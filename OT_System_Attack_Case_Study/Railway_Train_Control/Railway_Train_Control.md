# OT Railway System Development [05]

![](img/s_01.png)

### Design of the Train Control for a Land-Based Railway Cyber Range

```python
# Author:      Yuancheng Liu
# Created:     2025/06/29
# Version:     v_0.0.1
# Copyright:   Copyright (c) 2025 Liu Yuancheng
```

**Table of Contents**

[TOC]

------

### Introduction

In modern railway systems, train control involves a complex integration of automation, signaling, and communication technologies. This article presents the design of a simplified train control system implemented within a land-based railway cyber range for the purpose of cybersecurity exercise, training and simulation. 

The simulated train system aims to provide a functional, interactive sub-system models ten autonomous 750V-DC trains operating on three separate tracks. Each train is equipped with an onboard Programmable Logic Controller (PLC) and Remote Terminal Unit (RTU), allowing it to autonomously interact with the trackside signaling systems. These trains are capable of navigating junctions and forks, docking at stations, and departing automatically, emulating key behaviors of real-world operations. To support cyber-physical attack and defense scenarios, the simulation includes realistic control logic, communication protocols, and monitoring interfaces.

This article is structured into four main sections:

- **Overview of the Train Simulation System** – Describes the role and architecture of the train simulation within the cyber range.
- **System Design of the Simulated Train** – Details the train’s auto control circuit design, PLC/RTU control sequence work flow, and signal interaction logic.
- **Network and Communication Configuration** – Explains how the simulated trains communicate over the on-train internal network and the railway SCADA network with signaling systems and HQ control center.
- **Train Control Interfaces** – Introduces the user interfaces including the onboard driver console and the HQ central monitoring HMI system.

This design serves as a foundational component in cyber range exercises, enabling red and blue teams to explore vulnerabilities and defense mechanisms in railway control environments.

> **Important**: The actual train control systems are highly sophisticated and governed by strict safety standards, the implementation described in this article offers a simplified conceptual model tailored for educational and training purposes in a controlled cyber range environment.



------



