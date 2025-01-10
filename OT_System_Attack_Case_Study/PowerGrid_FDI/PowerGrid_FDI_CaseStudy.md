# Power Grid Simulation System 02 : FDI Power Outage Attack Case Study

We are excited to share that the [Power Grid Simulation System](https://www.linkedin.com/pulse/power-grid-ot-simulation-system-yuancheng-liu-dpplc/?trackingId=hN%2Ftqii0T5yoT12GO8pJZg%3D%3D) we developed was used as part of one red team's targeted critical infrastructure system the international cyber exercise [Crossed Swords 2024](https://ccdcoe.org/exercises/crossed-swords/) which conducted in December 2024. In this article, we will introduce one power outage attack case study which use the Power Grid Simulation System as the demo platform for OT cyber security workshop.

![](img/logo_small.png)

**Project Design Purpose**: This case study demonstrates using the Power Grid Simulation System as a target critical infrastructure to showcase the implementation of a **False Data Injection (FDI) attack** on the electricity Electrical Metering Unit (MU) readings of a power grid's Remote Terminal Unit (RTU). The attack scenario focuses on manipulating voltage or current reading value by overwriting the specific memory addresses data within the RTU, thereby triggering the safety protection mechanisms of the SCADA system. This process ultimately leads to a power cut-off for a primary power customer which is the railway system connected to the grid's Level 0 step-down transformer. 

This particular attack scenario is proposed as one of the demonstration cases for the Crossed Swords 2024 Test-Run, serving as a live demonstration of how an IT intrusion can disrupt and potentially paralyze critical OT infrastructure. It highlights the devastating consequences of cyberattacks on industrial control systems and emphasizes the importance of robust cybersecurity measures for safeguarding critical infrastructure.

- **Attacker Vector** :  ` Siemens-S7comm Protocol False Data` , `Command Injection` , `Powe outage attack`
- **Matched MIRTE-CWD**:
- **Mapped MITRE-ATT&CK-TTP**:

> Important : The demonstrated attack case is only used for education and training for different level of IT-OT cyber security ICS course, please don't apply it on any real world system.

```
# Created:     2025/01/08
# Version:     v_0.1.4
# Copyright:   Copyright (c) 2025 LiuYuancheng
# License:     GNU Affero General Public License v3.0  
```

**Table of Contents**

[TOC]

------

### Introduction

This case study demonstrates the execution of a **Siemens-S7Comm False Data Injection (FDI) attack** on a power grid system's SCADA network, illustrating how an attacker can exploit vulnerabilities to cause a power failure for a critical infrastructure client: a land-based railway simulation system connected to the Level 0 power distribution system. The attack process is divided into two main phases:

- **IT System Attack**: This phase covers how the attacker uses a trojan to achieve lateral movement, evade intrusion detection systems (IDS), and deliver the OT attack payload (FDI script) to a compromised machine with access to the SCADA network. 
- **OT System Attack**:  This phase illustrates how the FDI script manipulates the power grid RTU’s memory, causing system errors that trigger the safety protection mechanisms, ultimately cutting off power to the critical infrastructure.

The attack progresses through nine key steps, as outlined in the case study overview diagram below:

![](img/title.png)



For the case study attack demo video, please refer to this link: https://youtu.be/INDEzA4qk7I?si=eG4ahl96KFb_Hv6u. 

#### Scenario Overview Introduction

In this case study, we envision a scenario where a red team attacker infiltrates the OT-System SCADA supervision network by implanting a **spy trojan** via an IT-based attack, such as a phishing email targeting a maintenance engineer's laptop. The attacker uses this trojan’s Command-and-Control (C2) capabilities to deliver a Siemens-S7Comm FDI script to a compromised machine within the SCADA network. The attack proceeds by:

1. Exploiting the spy trojan to download FDI attack script into a victim node which can connect to the power system RTU.
2. Bypasses verification functions and manipulating voltage or current reading value to generate exception data.
3. Triggering the power grid system’s protection mechanism, leading to the disconnection of the transformer’s energy supply to the critical infrastructure customer.

This case study incorporates three key sub-projects:

- **Mini OT-Energy-System Cyber Security Digital Twin** : The primary demo platform used for attack execution, data collection, and visualization of the exception scenario demonstration .
- **Land Based Railway IT-OT System Cyber Security Digital Twin** : A railway digital twin simulate the Level 0 primary power distribution customer of the power grid, which drains 69kV AC with a maximum current of 100A for operation and used for show case the effect when the power outage attack happens.
- **Ninja_C2_Malware_Simulation_System** : An agent based trojan attack monitor and control system (includes the spy-trojan and the C2 Hub) used to control simulate the attack progress. 

#### Case Study Structure Introduction

In this case study, we will follow below flow diagram to draft the article. Beginning by introducing the digital twin systems used in the case study with background information to give a general overview. Then after providing related links for attack vectors and vulnerability, we will show the attack demonstrate and introduce the attack observation with the attack path. Finally we will map the system vulnerabilities to the MITRE CWE framework, and align the attack path with the MITRE ATT&CK framework for those looking to integrate this case study into their cybersecurity training programs.

![](img/s_03.png)

The case study document also includes the guidance for green team engineers deploying the simulation system's modules across various virtual machines (VMs) or physical devices. 

------

### Background Knowledge

Within this section, we aim to provide fundamental, general knowledge about each respective system and elucidate the Tactics, Techniques, and Procedures (TTP) associated with the attack vectors. This foundational information will serve as a primer for understanding the intricate details of the systems involved and the methodologies employed in the attack scenarios.

#### Power Grid Simulation System Over View

The **Mini OT Power Grid Simulation System** is a digital equivalent software platform designed to simulate the core operations of a hybrid power grid system, including hybrid power generation (natural gas power plants, solar power plants, and wind turbine farms), high-voltage power transmission and a three-level step-down power distribution system. The simulation integrates a SCADA system that incorporates PLCs for remote system control, RTUs and MUs for real-time data monitoring, and an HMI interface for operators to manage the grid. The system structure is shown below:

![](img/s_04.png)

To check the detail please refer to this link: [System introduction link](https://www.linkedin.com/pulse/power-grid-ot-simulation-system-yuancheng-liu-dpplc/?trackingId=hN%2Ftqii0T5yoT12GO8pJZg%3D%3D)



#### Land Based Railway IT-OT System Cyber Security Test Platform 

The land-based railway system is a miniature cyber range capable of providing a simplified and straightforward digital-twin style Operational Technology (OT) environments emulation solution for the railway track signaling systems, train ATC and ATP system, station control system and the IT environment to simulate the railway company’s corporate network. The system structure is shown below:

![](img/s_05.png)



#### False Data Injection (FDI) and False Command Injection (FCI)

Both FDI and FCI attacks target OT systems, FDI focuses on manipulating the data flowing through the system to deceive decision-making processes, while FCI involves injecting false commands to manipulate the actions of the control systems. Both types of attacks can have serious consequences, potentially leading to operational disruptions, safety hazards, or damage to critical infrastructure. Security measures, such as network segmentation, encryption, and intrusion detection systems, are crucial for protecting OT systems from these types of attacks.

**False Data Injection (FDI):**

- **Objective:** The main goal of FDI is to manipulate the data within the OT system, leading to incorrect or misleading information being processed by the control systems.
- **Method:** Attackers inject false or manipulated data into the sensors or communication channels within the OT system. This can lead to the control systems making incorrect decisions based on the compromised data.

**False Command Injection (FCI):**

- **Objective:** FCI aims to manipulate the commands sent to the control systems, causing them to execute unauthorized or malicious actions.
- **Method:** Attackers inject false or unauthorized commands into the communication channels or control signals of the OT system. This can lead to the control systems taking actions that are not intended or authorized.



#### Ninja_C2_Malware_Simulation_System

The Project Ninja is a cyber attack simulation toolkit designed for red team attackers to rapidly and dynamically develop and deploy various types of cyber attacks. The system is composed of a Command and Control (C2) hub and multiple distributed Trojan-Malware agents with below five main features:

- **Polymorphic Malware Construction:** A simple agent with a C2 tasks synchronization interface and a library of malicious activity plugins allows for customized construction of various types of malware.
- **Centralized Control and Task Distribution:** The C2 attack tasks synchronization mechanism enables attackers to dynamically control the functions of different Ninja malware agents.
- **Dynamic Malware Action Code Execution:** Users(red team attackers) can dynamically plug in attack modules or even execute code sections during malware runtime.
- **Camouflage Actions and Trace Erasure:** The system disguises attack actions and communications as normal software operations and erases traces to evade defender track logs.
- **Malware Self-Protection:** A self-protection watchdog prevents the malware from being terminated or deleted if it is detected by anti-malware software or defenders.

The system structure is shown below:

![](img/s_06.png)

To check the detail, please refer to this link: https://github.com/LiuYuancheng/Ninja_C2_Malware_Simulation_System



------

### Attack Scenario Design

The attack scenario demonstrates a **False Data Injection (FDI) attack** on a power grid system, leading to a power failure for the railway system. In this section, we will introduce the targeted vulnerable point of the system which used by the attacker and the attack path (lateral movement) of the attacker.

#### Attack Vulnerability Background 

As shown in the background knowledge section, the FDI focuses on manipulating the data flowing through the system to deceive decision-making processes. In the case study, the attack will aim on the power grid operating data collection and the exception situation handling part. The table below outlines the **normal operating ranges** for voltage and current across various power loads and customers within the power grid system. Each type of energy source has specific voltage and current thresholds that ensure safe and efficient operation.

| Energy Source                  | Connected System        | Voltage Range | Current Range |
| ------------------------------ | ----------------------- | ------------- | ------------- |
| High Voltage Transmission Line | Distribution Substation | 0 - 150 kV    | 0 - 120 A     |
| Level 0 Step-Down Transformer  | Railway System          | 0 - 80 kV     | 0 - 100 A     |
| Level 1 Step-Down Transformer  | Smart Factory           | 0 - 15 kV     | 0 - 90 A      |
| Level 2 Step-Down Transformer  | Smart Home              | 0 - 220 V     | 0 - 40 A      |

The following table provides details on the **RTU memory addresses index**(from `0x00000000`)  used to store power load data received from Metering Units (MUs). Each address corresponds to specific metering data for voltage and current, stored as integer values.

| MU Components                                          | Memory Address Index | Address      | Byte Index | Data Type |
| ------------------------------------------------------ | -------------------- | ------------ | ---------- | --------- |
| Distribution Substation Voltage                        | 6                    | `0x00000006` | 4          | Int       |
| Distribution Substation Current                        | 6                    | `0x00000006` | 6          | Int       |
| Level 0 Step-Down Transformer (Railway System) Voltage | 7                    | `0x00000007` | 4          | Int       |
| Level 0 Step-Down Transformer (Railway System) Current | 7                    | `0x00000007` | 6          | Int       |
| Level 1 Step-Down Transformer (Smart Factory) Voltage  | 8                    | `0x00000008` | 0          | Int       |
| Level 1 Step-Down Transformer (Smart Factory) Current  | 8                    | `0x00000008` | 2          | Int       |
| Level 2 Step-Down Transformer (Smart Home) Voltage     | 8                    | `0x00000008` | 4          | Int       |
| Level 2 Step-Down Transformer (Smart Home) Current     | 8                    | `0x00000008` | 6          | Int       |

These configurations ensure that the RTU correctly interprets and processes the data from the MUs, enabling efficient monitoring and control of power distribution across various systems. The attacker will use the above 2 functions as the vulnerable points then try to use the error data to overwrite the data saved in the related memory address to trigger the  transformers' voltage limitation feature. 



#### Attack Path Introduction

The process consists of 7 steps, as illustrated in the attack path diagram below.

![](img/s_07.png)

- **Step-01** : After successfully infiltrating the OT production network, the red team attacker discovers that the RTU can accept memory value modification commands via the `Siemens-S7Comm` protocol. The attacker then creates an S7Comm client program to continuously inject a high voltage value (100kV) into a specific RTU address which store the measured transformer's output voltage to the railway system, overriding the legitimate readings from the railway transformer’s metering unit.
- **Step-02** : The **Power Grid HMI** regularly reads data from the RTU. Each reading has an acceptable range, and if a value falls outside this range, the HMI will interpret it as an incorrect reading or a system error.
- **Step-03** : When the HMI detects a reading of 100kV for the railway operating voltage, which is outside the safety range of 0-72kV, it triggers an alert for the power grid operator to investigate.
- **Step-04** : If the power grid operator does not address the alert and the abnormal voltage reading persists three times consecutively, the SCADA-HMI will treat as a real system error and try activate its circuit protection mechanism. Typically, if the voltage or current is out of range, the circuit breaker trips immediately. However, if the high value persists for a period, it suggests a potential jammed of the breaker. After three alerts indicating high voltage, the HMI confirms an power error in the railway power system and initiates an automatic safety control to disconnect the railway transformer’s output, protecting the overall system.
- **Step-05** : The HMI sends a **Modbus-TCP command** to the PLC to remotely control the motorized circuit closer linked to the circuit breaker. For details on the design of the remote-controllable circuit breaker, refer to the following link: [Remote Controllable Circuit Breaker Design](https://github.com/LiuYuancheng/IT_OT_IoT_Cyber_Security_Workshop/blob/main/OT_System_Attack_Case_Study/Power_CircuitBreaker/Power_CircuitBreaker.md). Consequently, the physical circuit breaker in the power grid simulator is turned off, cutting off energy transmission to the railway system interface, resulting in 0V, 0A output.
- **Step-06** : The power grid physical simulator sends a **power cut-off message** to the railway system physical world simulator via the power link.
- **Step_07** : Upon receiving the power state update from the power link, the **railway system physical simulator** triggers power outage situation:  an emergency stop for all trains due to the loss of power. All trackers switch to a power failure state (red color), and the railway system displays a power outage alert.



------

