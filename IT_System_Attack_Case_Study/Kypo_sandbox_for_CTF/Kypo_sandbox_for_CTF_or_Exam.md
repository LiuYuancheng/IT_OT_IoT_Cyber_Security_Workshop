# CTF Challenge Write Up 02: The Secret Laboratory

**Design Purpose** : This article is the second write up of the using Kypo-CRP for building  CTF challenges or hands on exams environment. In this article I will use the Masaryk University Spring 2020 semester course PV276 CTF Cybersecurity game "Secret laboratory" as an example to show: 

- The detailed step to build your own or deploy exist CTF/Teaching-assignment  sand box on Kypo-CRP platform.
- The detailed steps of using the KYPO-CRP application and solving the PV276 Secret laboratory challenge.

The PV276 Secret laboratory CTF challenge is designed as up level Web and Information security training to introduce the penetration test workflow for a web attack defender, web service vulnerability identify and exploit ,  CVE attack,  and the information protection taught in Masaryk University Cybersecurity course [PV276 Seminar on Simulation of Cyber Attacks Course](https://is.muni.cz/course/fi/autumn2020/PV276). The Locust 3302 sandbox is publicly available as part of KYPO’s open-source releases on KYPO official Gitlab Repo [MUNI-KYPO-TRAININGS / games / secret-laboratory](https://gitlab.ics.muni.cz/muni-kypo-trainings/games/secret-laboratory) for people to practice hands-on cyber defense and offense techniques.



```python
# Author:      Yuancheng Liu
# Created:     2024/07/21
# Version:     v_0.1.2
# License:     MIT License
# Kypo-CRP Disclarmer: This training topic is for educational purposes only.The story is fictitious.
```

**Table of Contents**

[TOC]



------

### Introduction

Before diving into the technical details of how to solve the Locust 3302 Blackcat Challenge, I would like to acknowledge and express thanks to the CTF challenge authors - Stanislav Boboň, David Hofman, Jakub Smatana  for designing such an engaging and thought-provoking hands on assignment for cyber security education and contest. This challenge consists of six sequential tasks, each designed to test core cybersecurity skills across cybersecurity threats, network, Linux system security, encryption and decryption. After solve the challenge the participants will get below knowledge about: 

- Basic concept about network probing/scanning tools such as  **fping** and **Nmap**.

- Understand the Linux file system, ssh configuration, user and file permission configuration.

- How to do a simple penetration test for a web service to identify and exploit possible vulnerability by use the **CVE-2014-6271** information.

- How to use a permission mis-configured file to do  library hijacking/overwrite attack and privilege escalation







In the previous article [How to Deploy KYPO_CRP on OpenStack-YOGA](https://www.linkedin.com/pulse/how-deploy-kypocrp-openstack-yoga-yuancheng-liu-zmjhc), I introduced how to deploy KYPO CRP on your open stack cluster, this article will introduce the steps to create a sandbox environment on KYPO CRP for buildingand a de



https://gitlab.ics.muni.cz/muni-kypo-trainings/games/secret-laboratory





https://gitlab.ics.muni.cz/muni-kypo-images

