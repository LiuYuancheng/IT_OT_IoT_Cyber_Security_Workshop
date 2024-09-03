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

#### Performance Measurement

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









