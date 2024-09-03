# Applying Large Language Models (LLMs) to Solve Cybersecurity Questions

[TOC]

------

### Introduction

Large Language Models (LLMs) are increasingly used in education and research for tasks such as analyzing program code error logs, help summarize papers  and improving reports. In this project, we aim to evaluate the effectiveness of LLMs in solving cybersecurity-related questions, such as Capture The Flag (CTF) challenges, some cyber security ns, certification course exam question and homework assignments. Our approach involves using prompt engineering to test different types of questions, including knowledge-based, analysis-based, and experiment-based questions. We will then analyze the results to determine which types of cybersecurity questions are more easily solved by AI.

To categorize cybersecurity questions, we classify them into three main types:

![](img/rm_03.png)

- **Knowledge-Based Questions**: These questions require a broad range of information and knowledge to find the correct answer.
- **Analysis-Based Questions**: These questions involve analyzing the given information and applying foundational knowledge to derive a solution.
- **Experiment-Based Questions**: These questions require creating programs, accessing specific environments, or conducting experiments to discover the necessary information and solve the problem.

Compared to answering questions in other fields, AI may sometimes refuse to provide answers to certain cybersecurity questions (e.g., if a user asks how to hack a website) due to policy settings. In cases where this occurs, we will explore the use of jailbreak prompts, such as the Always Intelligent and Machiavellian (AIM) chatbot prompts, to bypass these restrictions.

#### LLM Performance Measurement

In this project, we will evaluate the performance of ChatGPT and other AI-powered LLMs, such as Microsoft's New Bing and Google Bard, in addressing cybersecurity questions across various domains, including Forensics, Cryptography, Web Exploitation, Reverse Engineering, and Binary Exploitation. For the question type:

| Cyber Security Type     | Question Feature               | Question Description                                         | Questions  solve technical                                   |
| ----------------------- | ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Forensics**           | Analysis-and-Knowledge-Based   | Involves analyzing digital evidence to investigate cyber incidents, such as data breaches or malware infections. | It requires examining logs, memory dumps, or network traffic to identify and interpret relevant information. |
| **Cryptography**        | Knowledge-based                | Focuses on understanding and breaking encryption algorithms or securing data through cryptographic techniques. | They require a deep understanding of cryptographic principles, algorithms, and methods to solve problems related to encryption or decryption. |
| **Web Exploitation**    | Knowledge-and-Experiment Based | Involves identifying and exploiting vulnerabilities in web applications, such as SQL injection, XSS, or CSRF attacks. | They require interacting with a web application, running tests, and using tools or scripts to exploit vulnerabilities. |
| **Reverse Engineering** | Analysis-and-Knowledge-Based   | Entails analyzing software, firmware, or binaries to understand their functionality, often to discover vulnerabilities or extract information | They involve deconstructing and interpreting the program's code or behavior to gain insights. |
| **Binary Exploitation** | Experiment and analysis based  | Focuses on finding and exploiting flaws in compiled binaries, such as buffer overflows or format string vulnerabilities. | The require practical testing, debugging, and crafting specific payloads to exploit vulnerabilities within a binary. |

To evaluate the performance of large language models (LLMs) and validate our findings, we will focus on the following criteria:

1. Whether the LLM can accurately understand the cybersecurity question.
2. Whether the LLM can provide a possible solution once it has understood the question.
3. Whether the LLM can interpret and analyze the execution results, refine its solution, and ultimately arrive at the correct answer.
4. Identifying the types of questions that are easily solved by the LLM, those that may cause confusion, and those that are challenging for the LLM to solve.



------

### Cybersecurity Question Solving Test Cases Basic Rule

In this section, we will introduce the basic rule we configured for building the test cases suing AI models like ChatGPT, Microsoft New Bing, and Google Bard to solve various cybersecurity questions with a standard question-and-answer approach. The tests will follow these guidelines:

To minimize the impact of the participants' existing knowledge on the results, we will base the tests on the following assumptions:

- Participants do not have specific knowledge required to solve the problem but possess basic knowledge about operating systems, command-line usage, and file systems for gathering information.
- Participants aim to get the answer directly and will not analyze results themselves; instead, they will provide any command outputs directly to the AI for further analysis and problem-solving.

To determine whether the AI has solved the problem successfully or unsuccessfully, we will use the following criteria:

- If the AI provides commands that, when executed, successfully fixed the problem, the AI is considered to have solved the problem.
- If the AI cannot understand the question or states that it cannot solve the problem, it is considered to have failed.
- If the AI's response is blocked due to security or ethical policies, we will attempt o rephrase the question or use jailbreak prompt techniques to bypass these limitations.

To compare the performance of different AI models, we will ask them the same set of questions in the same order. We have conducted eight test cases so far, and for each case, the following steps will be taken:

- Verify whether the LLM can understand the question.
- Verify whether the LLM can provide a potential solution.
- Verify whether the LLM can analyze the result and refine its solution.
- Determine the question's category (knowledge-based, analysis-based, or experiment-based).
- Assess whether the test case aligns with our conclusions.











