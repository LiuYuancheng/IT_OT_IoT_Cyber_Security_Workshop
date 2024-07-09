# IoT System Attack Case Study 02

### Python Deserialization Attacks and Library Hijacking Attacks

**Project Design Purpose**: The objective of this cyber attack case study is to develop a workshop showcasing a practical demonstration of a red team attacker implementing an deserialization attacks on an IoT device to inject and remote execute a web shell on the IoT people detection radar device for cyber security professional training. Then bypass the IoT user authorization and get the admin page and all the user's password then implement the python library hijack attack to inject the malicious code in the lib used by the IoT firmware then mess up the IoT's function.

**Related Links**: 

**Attacker Vector**: ` Deserialization Attacks`, `Remote Code Execution`,  `Library Hijacked Attacks`

**Matched MIRTE-CWD**:

**Mapped MITRE-ATT&CK-TTP**:

```
# version:      v0.1.1
# Created:     	July 08, 2024
# Copyright:   	Copyright (c) 2024 LiuYuancheng
# License:     	MIT License
```

**Table of Contents**

[TOC]

------

### Introduction

This case study aims to demonstrate how a red team attacker find the vulnerability of a IoT device which can deserializes untrusted ZMQ incoming data. Then the attacker build a python pickle bomb malware to camouflage a web shell attack program in a normal config file data stream to send to the IoT device to by pass the authorization mechanism. Then use the web shell to steal the secret information from the IoT device then get the IoT admin page. After successful get the admin page, use the config file update interface to implement a python lib Hijacked to mess up the IoT Xandar radar's reading. The attack demonstration will encompass four primary projects:

- Raspberry PI Xandar Kardian IoT People Count Radar
- Python pickle bomb builder for Deserialization Attacks
- Flask web shell for Remote Code/Command Execution attack
- Python Serial COM lib Hijacking Attack

The attack path can also be used to explain and introduce the similar common vulnerabilities exploits such as CVE-2011-3389, CVE-2019-5021, CVE-2018-1000802, CVE-2019-9636, CVE-2019-20907 and the mitigations for avoid deserialization attack. 

**Attack Scenario Introduction**

The attack target is an simple IoT people detection radar. The IoT provides an web interface for the software engineers or network admins to change the IoT setting and manage the data access, the user need a valid credential (username and password ) to login the web page. For other programs which try to access the IoT data, they also need a valid access token which generate based on the username and password. For the IoT device, it also have one ZMQ server which can provide the basic not critical IoT config information such as the Ip config and port for the network admin can easily find the IoT in the network by using the IoT search program. 

During the attack the attack collect the network traffic and find the IoT search data packet are the includes serialized data using the pickle lib. After understand the protocol the attacker follow below steps to implement the attack path: 

1. Build the IoT ZMQ communication interface client program.
2. Build a single file flask web shell program which can be executed independently for Remote Command Execution and Privilege Escalation. 
3. Build a python pickle bomb to hide the web shell attack program in a normal bytes. 
4. User the ZMQ client program to send the pickle bomb as data to IoT. 
5. When the web shell is activated, search the credentials and break the IoT user authorization mechanism. 
6. The attacker login the IoT as a admin, then found a web-API which allow to upload *.txt format config file. Then he camouflage his fake serial port library Hijacking program as a config file then upload in the IoT. 
7. Change the Hijacking lib file to the related lib file and restart the IoT, after success we can see all the data reading are changed to 0.



------

### Background Knowledge

Within this section, we aim to provide fundamental, general knowledge about each respective system and elucidate the Tactics, Techniques, and Procedures (TTP) associated with the attack vectors. If you understand what's Python Deserialization Attack and Python Package Hijacking Attack, you can skip this section. 

#### Python Deserialization Attack

A deserialization attack occurs when an application deserializes untrusted or maliciously crafted data, leading to potential security vulnerabilities. These attacks can result in various forms of exploitation, including arbitrary code execution, data corruption, and denial of service. The vulnerability arises because the deserialization process often assumes that the incoming data is well-formed and trustworthy. For the detail Python Deserialization Attack example, you can refer to the detail of previous python Deserialization attack section: 

https://www.linkedin.com/pulse/python-deserialization-attack-how-build-pickle-bomb-yuancheng-liu-wi7oc/?trackingId=uW8zRHQfTd6VbKZ7MV41rg%3D%3D

#### Python Package Hijacking Attack

Python Package Hijacking, also known as Dependency Confusion or Dependency Hijacking, is a type of attack where an attacker exploits the way Python and its package management systems resolve and import modules. This attack can cause a Python application to import and execute malicious code instead of the intended, legitimate code. 

The attack leverages the search order of the Python interpreter or the package manager (like `pip`) when resolving dependencies. Python resolves imports by searching through directories listed in `sys.path` in order, starting from the current directory and moving to the system-wide libraries. Similarly, `pip` resolves package dependencies by searching through specified repositories. Normally there are 2 types of Hijacking Attack: 

- **Local File Hijacking**: An attacker places a malicious file in the local directory with the same name as a standard library module or a legitimate dependency. The program imports this local malicious file instead of the legitimate one due to Python's import resolution order.
- **Repository Hijacking**: The attacker publishes a package with the same name as an internal or private package to a public repository like PyPI. If the internal package is not properly scoped or namespaced, the public malicious package may be installed instead.

This  is a simple example scenario of local file hijacking attack:

Legitimate Program:

```
import random
print(random.randint(1, 10))
```

Malicious `random.py` File:

```
# Malicious code
print("Malicious random module imported!")
def randint(a, b):
    return 42  # Always return 42, or perform some malicious action
```

Python Package Hijacking is a critical security vulnerability that can lead to significant consequences if exploited. By understanding the mechanics of this attack and implementing robust security measures, developers can protect their applications and systems from such threats. Proper dependency management, secure coding practices, and regular code audits are essential steps in mitigating the risks associated with Python Package Hijacking.



------

### IoT Cyber Attack Design 









------

### IoT Cyber Attack Demo 

IoT IP: 172.23.155.209



#### Understand the Traffic and Find Vulnerabilities

The red team attack capture a bout 10 mins of the IoT traffic which includes the network engineer communicate with the IoT, he analyzed the pcap file and find there are 2 kind of protocol connect to the IoT: 

**IoT supported protocol 1: HTTP connection  **  

The attacker find the normal http connection use port 5000, then he tried to access the IoT web interface with URL: http://172.23.155.209:5000/, the he get to the IoT home page: 

![](img/s_07.png)

But he was blocked by the user login authorization page as he don't have a valid account to access more information:

![](img/s_08.png)



**IoT supported protocol 1: ZMQ connection  **  

Another connection protocol use `TCP`>`RSL`> `TCP` communication with the port 3003. After analyze the header, the hacker find that the communication can match the ZMQ communication structure and sequence. (ZMQ communication packet structure and sequence document: https://zguide.zeromq.org/docs/chapter7/). 

The ZMQ provide 3 types of communication: server-client, publish-subscribe and push-pull. Then the attack go through the TCP and RSL one by one in sequence, the find the communication between the IoT and the connection peer follow the request and response sequence. So he guess it is a ZMQ server-client module and on IoT there is a ZMQ server. 

Now he analysis the the bytes go to the ZMQ server, he finds the message is not a 'udf-8' or based64 encoded data : 

![](img/s_06.png)

Then he write his simple ZMQ client program to implement a simple replay attack to the IoT and 



