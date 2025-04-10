# Reverse Engineering to Get the Malware Source Code via Memory Dump in DFIR

This article will introduce the detailed steps about how to parse a complied windows malware exe file (coded by python) from the windows memory dump file then decompile the data to get the source code for a DFIR (Digital Forensics and Incident Response) cyber exercise. The article includes below 5 section.

1. Create a python windows execution file. 
2. Configure the windows for memory dump collection. 
3. Collect the memory dump file. 
4. Parse the memory dump to get the executed malware data. 
5. Decompile the malware data back to sour



------

### Introduction

The Digital Forensics and Incident Response is a very wide topic in cyber execise/event, this article is included in the Memory forensics topic in DFIR (as shown below). Before we start, we need to introduce some background knowledge about the DFIR and the tools we used. 

![](img/s_02.jpg)

**Digital forensics and incident response (DFIR)** is a field within cybersecurity that focuses on the identification, investigation, and remediation of cyberattacks.

DFIR has two main components:

- **Digital forensics:** A subset of forensic science that examines system data, user activity, and other pieces of digital evidence to determine if an attack is in progress and who may be behind the activity.
- **[Incident response](https://www.crowdstrike.com/en-us/cybersecurity-101/incident-response/):** The overarching process that an organization will follow in order to prepare for, detect, contain, and recover from a [data breach](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/data-breach/).

The [Digital forensics](https://www.crowdstrike.com/en-us/cybersecurity-101/data-protection/digital-forensics/) provides the necessary information and evidence that the computer emergency response team (CERT) or computer security incident response team (CSIRT) needs to respond to a security incident. Digital forensics may include: File system forensics, Memory forensics, Network forensics and Log analysis

