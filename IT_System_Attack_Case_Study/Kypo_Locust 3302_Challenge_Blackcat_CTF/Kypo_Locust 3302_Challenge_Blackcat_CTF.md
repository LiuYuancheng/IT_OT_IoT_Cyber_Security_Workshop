# Write Up of KYPO Locust 3302 Challenge of Blackcat_CTF

**Design Purpose** : In the previous article *[How to Deploy KYPO_CRP on OpenStack-YOGA](https://www.linkedin.com/pulse/how-deploy-kypocrp-openstack-yoga-yuancheng-liu-zmjhc)*, I introduced how to deploy KYPO CRP on Open Stack cluster. This write-up will focus on the detailed steps of using the KYPO-CRP application and solving practical CTF questions through the KYPO Locust 3302 Challenge which used in the Blackcat CTF [Hacker and Defender Training] developed by Masaryk University’s Cybersecurity. 

This CTF challenge is designed as an advanced Web and Information security exam to test the CTF participants through  penetration testing workflows, web service vulnerability exploit , command injection attack and the information protection knowledge and skills taught in Masaryk University Cybersecurity course [PV276 Seminar on Simulation of Cyber Attacks Course](https://is.muni.cz/course/fi/autumn2020/PV276) . The Locust 3302 sandbox is publicly available as part of KYPO’s open-source releases on KYPO official Gitlab: [MUNI-KYPO-TRAININGS / games / locust-3302 · GitLab](https://gitlab.ics.muni.cz/muni-kypo-trainings/games/locust-3302) for people to practice hands-on cyber defense and offense techniques.

```python
# Author:      Yuancheng Liu
# Created:     2024/03/20
# Version:     v_0.1.2
# License:     MIT License
# Kyppo Disclarmer: This training topic is for educational purposes only.The story is fictitious.
```

**Table of Contents** 

[TOC]

------

### Introduction 

Before starting with the technical details of how to solve the Locust 3302 Blackcat Challenge, I want to express thanks to the challenge authors Adam Chovanec, Hana Pospíšilová, Peter Jaško for creating the interesting and challenging CTF challenge Question. The challenge includes 6 questions which covers the knowledge of cybersecurity threats, network, Linux system security, encryption and decryption. The CTF participants needs to solve them with blew actions: 

- penetration test and web security: Conduct penetration testing using suitable tools such as Metaploit to identify the possibility vulnerability of a web service.
- command injection attack: How to use command injection introduce in CVE-2019-15107 to attack the Webmin service (password_change.cgi) to start a web shell then check the webhost’s critical information. 
- Linus system Critical information analysis : How does the hacker find the secret information by tracing the the user’s bash cmd history. [ ]
- Encryption and decryption, information protection: How to use the password cracking software tool John the Ripper(ssh2Jhon) to crack SSH private Key’s passphrase. 

#### Challenge Background Story

When login the KYPO challenge page, the background storage is shown

![](img/s_03.png)

Infosec community all over the word has been investigating hacker group Black cat. This mysterious organization has been very active in the hacker scene and is believed to be responsible for several cyber-attacks.Recently you have acquired an IP address of one of their servers. Find out who they are and what do they do. These criminals have to be stopped!"

#### Environment network topology

There are three VMs in 3 subnets as show below:

![](img/s_04.png)

- Attacker (10.10.135.83) is the student's practice VM which student can login with sudo permission, all the hacking tools are installed in this VM, the student can use this VM to attack the other 2 VMs in the other two subnets. 
- Web VM (172.18.1.5) in "outside-network" is simulating a web-server host Webmin web-service, it is hidden for the students.  
- Client VM (10.1.17.4) behind "big-broker" subnet is a secret server which another hacker transferred the web host file to, the students need to find its IP by search and analysis the web-server's related information. so it is hidden for the student.   

#### CTF Questions Techniques

The challenge contents 6 questions under linear sequence, the CTF participants needs to solve then one by one, the main technical for each questions are: 

- **Q1[Scan the IP address and port]** : The player will be orient in Kali Linux and its tools, learn how to use Nmap to scan a specific ipaddress' ports to find the program which is hosting some service. In this section they need to find the web-based system administration tool for Unix-like servers Webmin running in the target network.
- **Q2[Identify a vulnerability]** : The player needs to use  penetration testing tool set Metasploit to identify the vulnerability of a service (web) and find the related CVE for exploiting the vulnerability.
- **Q3[Exploit the vulnerability]** : The participants need to use basic metasploit function console and use CVE to exploit a web service with command injection attack.
- **Q4 [Find an IP address of the secret server]** : The player need the check the hacker can trace and analysis the command history of linux system to get the critical information.
- **Q5[Access the secret server]** : How to use the password cracking software tool John the Ripper(ssh2Jhon) to crack SSH private Key’s passphrase.
- Q6[Steal secret information from the other server]: The CTF player needs to find how to change the private key permission to login the server and get the secret data.

