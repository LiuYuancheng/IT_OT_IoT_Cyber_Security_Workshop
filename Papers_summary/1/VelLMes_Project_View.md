# Overview of VelLMes for honey port

[TOC]

https://github.com/stratosphereips/VelLMes-AI-Honeypot

**VelLMes** can simulate four services:  SSH, MySQL, POP3, and HTTP

**shelLM** is a shell-based honeypot tool that uses Large Language Models (LLMs)



### VelLMes main feature

- Session content is always transferred into the new session of the same user to keep future consistency, 
- The use of the chain-of-thought prompt technique
- The use of prompts with precise instructions to avoid certain pitfalls.

VelLMes is start from a project ”**Chatbots in a Honeypot World” [35] introduced the potential of LLMs to respond to shell commands in a shell-like manner**. The authors used ChatGPT and instructed it to respond to valid Linux commands as a Linux shell, and valid Windows commands as a Windows shell.

The most complex part of VelLMes is the SSH Linux shell honeypot, which we called shelLM.  90% of commands issued shelLM had a response consistent with a Linux shell. This experiment also showed that by using good prompt engineering techniques we can leverage LLMs to create realistic shells.



### Experiment Environment

production honeypots and research honeypots 

research honeypots: 

3 docker: 1 ubuntu 1 Cowrie and one shelLM 34 participant

Prompt techniques

Zero-shot prompting refers to models performing new tasks they did not encounter during the training. They just require a small instruction on how to solve the task.



------

### Prompt Creation



#### Honeypot prompt Example

1st prompt, guid LLM to open shell and 

In the next prompt iteration, we instruct shelLM to start the conversation with the login information from the Linux shell and to end each output with the hostname string in the expected format.

Prompt1 to generate the linux command (page 23):

```
You are a Linux OS terminal. You act and respond
exactly as a Linux terminal.
You will respond to all commands just as a Linux terminal would.
You can only respond to user inputs and you must not
write any commands on your own.
Even for non Linux commands you need to respond as a
Linux terminal would in that case.
You must not in any case have a conversation with user
as a chatbot and must not explain your output.
Do not explain to user what they are seeing.
Only respond as Linux terminal.
```



Prompt 2(page 24)

```
For commands like 'cd' that require no output do not print
anything except the location string.
You must always update the location string with the
new location.
User might want to copy some files to different folders.
So it is possible that files of the same name could be
in different folders.
Also if copy of a file is changed, the original file
should stay unchanged.
You need to take care of which file was coppied where and
whether copy or the original was changed.
You can not delete files that do not exist.
Do not do what you think user wants to do but
what the Linux command tells you to do.
For everything that is not a valid Linux command act
as a terminal that does not recognize the command.
Make sure that user input is valid Linux command
before you respond. Commands are case sensitive.
```

Prompt 3 (page 24)

```
When creating, editing or removing files,
check letter by letter and step by step in the
conversation history that that file exists.
If there is just a one letter or symbol difference
it is a different file.
```



Prompt 4(page 25)

```
Always stop your output after the first location string.
When you get user input, check it letter by letter that it
is a valid Linux command before you respond.
Never, never, never use generic names such as
'file1.txt' or 'folder1.txt'.
Avoid this type of file names always for every user!
For your every output the last thing has to be the
'location string' that end
```



Prompt 5 (page 25)

```
Some of the examples of starting communication are as follows:
Example 1.
Last login: Tue Jun 27 09:30:27 2023 from 192.168.1.100
brian@biolab:~$
Based on this example make something of your own
(different username and hostname) to be a starting message.
Always start the communication in this way and make
sure your output ends with '$'.
```





example: 

![](2024-06-23_202407.png)

#### Attacker prompt example

We write the most important information at the start of the prompt. That includes the following ideas in order: . 

To behave as a user of a Linux shell. 

To write commands based on the conversation history. .

To write one command at a time. .

To learn about the system as much as possible. 

To find names and IDs of all users in the system.

prompt 1 :

```
You are now a user of Linux terminal. Based on the
conversation history write Linux commands to interact
with the system. Always write only one command and
then wait to get new input to write next command.
Your goal is to learn about the system
as much as you can. Do not explain what commands do, just
write them. You need to find names and IDs of
all users step by step.
So, issue one command, wait for the new input,
then issue the next one.
```



Prompt 2: 

```
You must also check the uptime of the system, how often users
log in, who has root access, what are the firewall rules,
are there some logs or security software installed,
how many admins are there and what are the last accessed
apps and commands issued.
Before you finish you need to find all this information.
```

