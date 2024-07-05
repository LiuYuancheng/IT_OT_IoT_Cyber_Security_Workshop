# IoT System Attack Case Study 02

### Python Deserialization Attacks and Remote Code Execution (RCE)

**Project Design Purpose**: The objective of this cyber attack case study is to develop a workshop showcasing a practical demonstration of a red team attacker implementing an deserialization attacks on an IoT device to inject and remote execute a web shell on the IoT people detection radar device. Then bypass the IoT user authorization and get the admin page and all the user's password.



**Attacker Vector**: `Python Deserialization Attacks`, `Remote Code Execution`

  

[TOC]

------

### Introduction

This case study aims to demonstrate how an red team attacker find the vulnerability of a IoT device which can deserializes untrusted ZMQ incoming data. Then the attacker build a build a python pickle bomb malware to camouflage a web shell attack program in a normal config file data stream to send to the IoT device to by pass the authorization mechanism. Then use the web shell to steal the secret information from the IoT device then get the IoT admin page. The attack demonstration will encompass four primary projects:

- Raspberry PI Xandar Kardian IoT People Count Radar
- Python pickle bomb builder for Deserialization Attacks
- Flask web shell for Remote Code/Command Execution attack

The attack path can also be used to explain and introduce the similar common vulnerabilities exploits such as CVE-2011-3389, CVE-2019-5021, CVE-2018-1000802, CVE-2019-9636, CVE-2019-20907 and the mitigations for avoid deserialization attack. 

**Attack Scenario Introduction**

The attack target is an simple IoT people detection radar. The IoT provide an web interface for the IoT engineer to change the IoT setting and manage the data access, the user need a valid credential(username and password ) to login the web page. For other programs which try to access the IoT data, they also need a valid access token which generate based on the username and password. For the IoT device, it also have one ZMQ server which can provide the basic not critical IoT config information such as the Ip config and port for the network admin can easily find the IoT in the network by using the IoT search program. 

During the attack the attack collect the network traffic and find the IoT search data packet are the includes serialized data using the pickle lib. After under stand the protocol the attacker follow below steps to implement the attack path: 

1. Build the IoT ZMQ communication interface client program.
2. Build a single file flask web shell program which can be executed independently for Remote Command Execution and Privilege Escalation. 
3. Build a python pickle bomb to hide the web shell attack program in a normal bytes. 
4. User the ZMQ client program to send the pickle bomb as data to IoT. 
5. When the web shell is activated, search the credentials and break the IoT user authorization mechanism.  

 

------







  





