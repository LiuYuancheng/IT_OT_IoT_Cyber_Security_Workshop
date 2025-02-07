# Deploy DeepSeek-R1 Locally and Build a Local RAG Knowledge Base

DeepSeek, a Chinese AI firm, is disrupting the industry with its low-cost, open source  large language models, challenging U.S. tech giants. It has shown high performance in mathematic, coding, English and Chinese Conversation. The DeepSeek-R1 model  is opensource ( MIT License ), this article will introduce how to deploy the DeepSeek-R1 on your local machine with a customized Retrieval-Augmented Generation knowledge base so the LLM can use some specific knowledge to solve problem which can art as an expert in some technical field, such as you can build your own support AI chat robot, code generation without upload your private document, information or licensed program to deep seek or add the information which is not in the deep seeks' learning data or not in public internet.

```python
# Version:     v_0.0.1
# Created:     2025/02/06
# License:     MIT License
```

**Table of Contents**

[TOC]

------

### Introduction

This article will use a normal laptop Window-PC with NVIDIA RTX3060(12G) to local deploy a deepseek-R1 7b LLM model with detailed document RAG data to build a customized information service chat robot or a program code builder. For the chat robot we want the AI can provide the information based on the company's product documents and for the code builder, we want the AI can give the code which based on the exist program API or import the exist function from the customized lab. 

To implement this project, we need 4 tools / program : 

- **Ollama** : a lightweight, extensible framework for building and running language models on the local machine.
- **DeepSeek-R1** : a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step, demonstrated remarkable performance on reasoning. 
- **nomic-embed-text** : an open-source text embedding model that converts text into numerical vectors, allowing computers to understand the semantic meaning of text by comparing its representation to others.
- **AnythingLLM** : an open-source AI chatbot that allows users to chat with documents. It's designed to help businesses and organizations make their written documents more accessible. 

#### Background Knowledge of RAG

Retrieval-augmented generation is a technique for enhancing the accuracy and reliability of generative AI models with information from specific and relevant data sources. The work flow of RAS is shown below:

![](img/s_03.png)

- In the **Normal LLM Question-Answer Flow** , when a user asks a question. Thee LLM processes the input and generates an answer **only based on its pre-trained knowledge**. There is no external data retrieval, meaning outdated or missing information cannot be corrected.
- In the **LLM with RAG Question-Answer Flow**, when a user asks a questions. The The system first retrieves relevant information from external sources (databases, documents, APIs, or the web). The retrieved data is fed into the LLM along with the original question, then the LLM generates an answer based on both **pre-trained knowledge and retrieved data**, leading to **more accurate and up-to-date responses**.

What is RAG: https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/

https://www.bilibili.com/video/BV16RF5eaEML/?spm_id_from=333.788.recommend_more_video.2



------

### Deploy DeepSeek-R1 Model on your Local machine

To setup the  DeepSeek-R1 Model on you Local, you need to install the Ollama Tool which is a lightweight, extensible framework for building and running language models on the local machine. Then download the related DeepSeek-R1 Model based on your hardware. 

To download the Ollama, go to https://ollama.com/download and select the installation based on your OS: 

![](img/s_04.png)

After installed the Ollama, open a terminal to verify the installation is successful with the version check cmd:

```
ollama --version
```

If the version number shows, which means the ollama is ready for use:

![](img/s_041.png)

Now you can start the ollama service with cmd:

```
ollama serve
```

Then in the Models search and find the deepseek model, there are different size models' ranging from compact 1.5 billion-parameter versions to the massive 671 billion-parameter model. Depending on the size of the model you intend to deploy and the hardware (especial GPU memory) you have, you can choose the one suitable for you.  We have list down the minimum requirements for hardware deploying different models below, you can also deploy a bigger model on low performance hardware by using the the hardware performance optimization tool such as LMStudio (https://lmstudio.ai/) , then the "thinking" time will be longer.

![](img/s_05.png)

DeepSeek-R1Hardware requirement

| Module Name      | Model Type Level | GPU VRAM                          | CPU                                                          | RAM         | Disk   |
| ---------------- | ---------------- | --------------------------------- | ------------------------------------------------------------ | ----------- | ------ |
| deepseek-r1:1.5b | Accessible       | No dedicated GPU or VRAM required | CPU no older than 10 years                                   | 8 GB        | 1.1 GB |
| deepseek-r1:7b   | Lightweight      | 8 GB of VRAM                      | Single CPU such as i5                                        | 8 GB        | 4.7 GB |
| deepseek-r1:8b   | Lightweight      | 8 GB of VRAM                      | Single CPU such as i5, i7                                    | 8 GB        | 4.9 GB |
| deepseek-r1:14b  | Mid-Range        | 12 - 16 GB of VRAM                | Single CPU such as i7, i9 or duel CPU such as Xeon silver 4114 x 2 | 16-32 GB    | 9.0 GB |
| deepseek-r1:32b  | Mid-range        | At least 24 GB of VRAM            | duel CPU such as Xeon silver 4114 x 2                        | 32 - 64 GB  | 20 GB  |
| deepseek-r1:70b  | Large-Scale      | 48 GB of VRAM                     | duel CPU such as Xeon gold 6130 x 2                          | 128-256 GB  | 43 GB  |
| deepseek-r1:671b | Large-Scal       | 480 GB of VRAM                    | duel CPU such as Xeon gold 6142 x 2                          | 512-1024 GB | 404 GB |

For 671b model: approximately 480 GB of VRAM. Multi-GPU setups are mandatory, with configurations such as:

- 20 Nvidia RTX 3090 GPUs (24 GB each)
- 10 Nvidia RTX A6000 GPUs (48 GB each)

Reference: https://www.geeky-gadgets.com/hardware-requirements-for-deepseek-r1-ai-models/, https://youtu.be/5RhPZgDoglE?si=xnHo9a9v7tvVd5sz

For my local configuration, I use a 3060GPU(12GB), so I can try the 7b. Then I can use the deepseek-r1:7b model, we can use the `ollama pull to down load the model`  or just use the run command, if the module is not download, ollama will auto download it:

```
ollama run deepseek-r1:7b
```

![](img/s_06.png)

Now the DeepSeek-R1has been setup on your local and you can ask AI questions from the terminal. 



------

### Install nomic-embed-text 

To build the RAG knowledge base, we need the nomic-embed-text to convert the data (such as PDF file, text strings) to vector data. To download the nomic-embed-text ,go to  https://ollama.com/library/nomic-embed-text and download the latest version as shown below:

![](img/s_07.png)

You can also use Ollama pull command to download it:

```bash
ollama pull nomic-embed-text
```



------

### Install AnythingLLM and Deploy RAG

Go to the anythingLLM web download page to download the installer based on your system:

![](img/s_08.png)



------

https://www.bilibili.com/video/BV16RF5eaEML/?spm_id_from=333.788.recommend_more_video.2