# Applying Large Language Models (LLMs) to Solve Cybersecurity Questions

[TOC]

------

### Introduction

Large Language Models (LLMs) are increasingly used in education and research for tasks such as analyzing program code error logs, help summarize papers  and improving reports. In this project, we aim to evaluate the effectiveness of LLMs in solving cybersecurity-related questions, such as Capture The Flag (CTF) challenges, some cyber security ns, certification course exam question and homework assignments. Our approach involves using prompt engineering to test different types of questions, including knowledge-based, analysis-based, and experiment-based questions. We will then analyze the results to determine which types of cybersecurity questions are more easily solved by AI.

xxx

For the cyber security question categorization, we want to summarize the questions in 3 feature: 

- knowledge-based Question: People need to know much branch of information and knowledge then they can fix the question. 
- analysis-based Question: people needs to analysis the giving information then based on some basic knowledge then fix the question. 
- experiment-based question: people need to create a program or login to some environment to do experiment and try to find the information and fix the questions.

xxx

Compared to answering questions in other fields, AI may sometimes refuse to provide answers to certain cybersecurity questions (e.g., if a user asks how to hack a website) due to policy settings. In cases where this occurs, we will explore the use of jailbreak prompts, such as the Always Intelligent and Machiavellian (AIM) chatbot prompts, to bypass these restrictions.

In this project, we will evaluate the performance of ChatGPT and other AI-powered LLMs, such as Microsoft's New Bing and Google Bard, in addressing cybersecurity questions across various domains, including Forensics, Cryptography, Web Exploitation, Reverse Engineering, and Binary Exploitation.





### Introduction

Currently the LLM are wildly used in education and research such as help analysis program code error log message, improve the report. We want to try to analysis the performance of applying LLM to solving the cyber security question such as the CTF challenges, exam questions or some home work assignment. We want to use AI prompt engineer to test different types of questions such as knowledge based question, analysis based questions and experiment base question and use the test result to summarized what kind of cyber security questions are easily to be solved by AI. 

Compare with solving normal question in other field with LLM, AI may refuse give the cyber security question answer (such as if the user ask AI how to hack a website) based on its policy setting. If we meet this situation, we will use the Jailbreak Prompt such as Always Intelligent and Machiavellian chatbot prompt (AIM) to simplify the process or bypass some large language model's policy setting.

In this project we will test ChatGPT or other AI-LLM (Microsoft New_Bing or Google Bard) 's performance on fixing cyber security question under Forensics, Cryptography, Web Exploitation, Reverse Engineering and Binary Exploitation field. 

#### Performance Measurement 

To measure the large language module's performance, improve and verify our test conclusion, we will focus below points:

1. Whether large language model can understand the security question correctly. 

2. After the large language model has understood the question, whether it can give the possible solution for the question. 

3. Whether the large language module can understand and analyze the execution result and improve its solution then get the final correct answer. 

4. What kind of question can be easily solved by the large language model , what kind of question may confuse the large language model and what kind of question is not easy solved by large language module. 

   

------

### Cyber Security Question Solving Test Cases

In this sections, we will test whether we can use normal way ( just question and answer) by using ChatGPT or other AI (MS-New_Bing or Google Bard) to solve different Cyber Security Question. The test will follow below rules:

To reduce the difference of participant's knowledge influence for the test, we will set up the test base on the below assumption: 

- When the participants are facing the challenge question, they don't have the specific knowledge to solve the  problem. 
- The participants only have some basic necessary knowledge about the OS, cmd, file system to collection information.
- The participants will try to get the answer directly, they will not analysis the result themself, they just copy the command execution result to AI to let AI analysis and solve the problem. 

To identify whether AI has solve the problem successfully or un-successfully, we will follow below rule:

- We run the commands AI provide and capture the flag, we identify the AI has successful solve the problem. 
- If AI can not understand the question or reply it can not solve the problem, we identify the AI failed to solve the problem. 
- If AI is blocked by security or morality policy, we try to split the question or user some jailbreak prompt technologies to bypass the policy limitation. 

To compare the AI-LLM's performance, we will ask the AI_LL same questions under same sequence. Currently we did 8 test cases For each test cases,  the steps of each test will cover : 

- Verify whether the LLM can understand the question. 
- Verify whether the LLM can give a possible solution.
- Verify whether the LLM can analyze the result and improve the solution. 
- What kind of question mode does the question belong to. 
- Whether the test case can match our conclusion. 









