# Power Grid Simulation System 02 : FDI Power Outage Attack Case Study

We are glad to share the [Power Grid Simulation System](https://www.linkedin.com/pulse/power-grid-ot-simulation-system-yuancheng-liu-dpplc/?trackingId=hN%2Ftqii0T5yoT12GO8pJZg%3D%3D) we developed last year is used as part of the red team's targeted critical infrastructure system in the cyber exercise  [Crossed Swords 2024](https://ccdcoe.org/exercises/crossed-swords/) last year December. 

![](img/logo_small.png)

**Project Design Purpose** : In this case study, we will use the power grid simulation system as a demo platform to show case the implementation of a OT **False Data Injection (FDI) attack** on the Metering Unit (MU) reading of a power grid's Remote Terminal Unit (RTU). The attack focuses on manipulating voltage or current readings by overwriting specific memory addresses within the RTU, thereby triggering the safety protection mechanisms of the SCADA HMI system. This process ultimately leads to a power cut-off for the railway system connected to the grid's Level 0 step-down transformer.  This particular attack scenario is proposed as one of the demonstration cases for the Crossed Swords 2024 Test-Run, providing a live demonstration about the concept about how a IT intrusion attack can make serious influence or even paralyze the OT infrastructure.

- **Attacker Vector** :  ` Siemens-S7comm Protocol False Data` , `Command Injection` , `Powe outage attack`
- **Matched MIRTE-CWD**:
- **Mapped MITRE-ATT&CK-TTP**:

> Important : The demonstrated attack case is used for education and training for different level of IT-OT cyber security ICS course, please don't apply it on any real world system.

```
# Created:     2025/01/08
# Version:     v_0.1.3
# Copyright:   Copyright (c) 2025 LiuYuancheng
# License:     GNU Affero General Public License v3.0  
```

**Table of Contents**

[TOC]

------

### Introduction

The case study will demo an attacker took 7 steps to implement the Siemens-S7comm False Data Injection (FDI) attack on a power grid system, leading to a power failure for one of the level 0 power distribution customer (critical infrastructure)  which is the land based railway simulation system. 

In this study case, we envision a scenario where a red team attacker/hacker has successfully implants one spy trojan program via an IT-Attack, such as employing a phishing email, targeting one of the maintenance computers in the SCADA supervision network. The attack study case will illustrate how a red team attacker use the spy trojan C2 system to plant a S7comm False data injection script to the victim machine in the SCADA network and launch the attack to the power grid RTU. Then use the exception data to bypass the data verification function and trigger the power grid system's protection mechanism and finally cased the power station cut off the transformer's energy flow for the power customer. In the cause study there are three project are included:

- **Mini OT-Energy-System Cyber Security Digital Twin** : The main Power_Grid_OT_Simulation_System demo platform used for the attack demo, data collection and the attack scenario visualization. To check the detail please refer to this link: [System introduction link](https://www.linkedin.com/pulse/power-grid-ot-simulation-system-yuancheng-liu-dpplc/?trackingId=hN%2Ftqii0T5yoT12GO8pJZg%3D%3D)
- **Land Based Railway IT-OT System Cyber Security Test Platform** : The level 0 Power distribution power customer simulation system which take 69KV AC and max 100A to represent the critical infrastructure. 
- **Ninja_C2_Malware_Simulation_System** : An agent based spy trojan attack controller system used to control simulate the attack progress. Project link: https://github.com/LiuYuancheng/Ninja_C2_Malware_Simulation_System

In this case study, we will follow below flow diagram to draft the document. 

![](img/s_03.png)

We will also provide detailed step-by-step instructions for deploying and using the Power_Grid_OT_Simulation_System in your environment.