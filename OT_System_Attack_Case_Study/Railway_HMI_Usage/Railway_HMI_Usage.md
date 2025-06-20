# OT Railway System Development [04]

![](img/s_01.png)

### Design and Usage of the Human-Machine Interfaces (HMI) for a Land-Based Railway Cyber Range

```python
# Author:      Yuancheng Liu
# Created:     2025/06/20
# Version:     v_0.0.1
# Copyright:   Copyright (c) 2025 Liu Yuancheng
```

**Table of Contents**

[TOC]

------

### Introduction

In the previous article, [*Implementing Different Human-Machine Interfaces (HMI) for a Land-Based Railway Cyber Range*](https://www.linkedin.com/pulse/implementing-different-human-machine-interfaces-hmi-land-based-liu-cqojc), we explored the development of four specialized SCADA HMIs designed for a land-based railway simulation cyber range. That article introduced the foundational concepts behind SCADA HMIs, the rationale for their implementation in cyber-physical environments, and the functional architecture tailored for this railway-specific use case. We concluded with an overview of the network topology and communication design for each HMI.

This article serves as the second installment in the HMI documentation series. In previous article, we end with the introduction of detail network and communication design of each HMI, here we move from conceptual design to practical implementation, providing a detailed look into how each of the four HMIs operates within the cyber range and supports hands-on cybersecurity exercises.

This article is organized into four key sections:

- **Software Structure Design**: A breakdown of HMI’s internal architecture, including control flow, modular design, thread management, asynchronous processing, and data handling.
- **Cyber Range UI Design**: An overview of the interface layout and user experience (UX) enhancements tailored for cyber exercise scenarios.
- **HMI Usage Introduction**: A practical guide to operating the HMIs for system monitoring, control, and responding to anomalies during cyber simulations.
- **Defense Case Study**: A demonstration of how an HMI, when integrated with intrusion detection systems (IDS), can aid in identifying and mitigating OT-specific cyber attacks and threats.

**Clarifying a Common Question**

Before diving into the technical content, let's clarify a frequent  question may ask when I introduce the OT cyber range: 

> Once the hacker get in to OT environment, it’s already too late -- defense is futile and the war is over. There is no point for OT engineers to be cyber security expert, purely the responsibility of IT to detect and defense the cyber attack, not OT engineers.

This viewpoint may be common for OT operators, but from a OT system manager's view it  underestimates the defensive capabilities present in modern OT systems and the crucial role of OT engineers. In reality, OT system includes complex protection , fault tolerance and redundancy mechanisms to avoid damage for different abnormal situation includes cyber attack. Such as the PLC-IP whitelisting, the use of static ARP entries, and tightly controlled communications protocols to make the ARP spoofing, Mitm nearly impossible.  Even after an initial breach, OT engineers who understand both the physical processes and security principles can still identify, analyze, and respond to attacks in time.

From the defender's view unlike IT environments, where traffic is often encrypted and obfuscated, OT networks exhibit highly deterministic behavior. This predictability allows abnormal traffic—such as unexpected mDNS queries, unsolicited HTTP requests, or rogue pings—to stand out clearly. Thus, with the right tools and training, OT engineers can become a first line of defense against cyber threats, making real-time visibility through HMIs a critical component of incident response.



------

### Software Structure Design

All the HMI programs are designed as a multi-threading with below architecture: 

![](img/s_02.png)

The main thread includes 5 sub modules:

- **Program Control Module**: Control the program execution and all the sub threads . 
- **Program Clock Control Module**: Control the loop frequency for all the other thread module and the display such as fps.
- **Program Data Control Module**: Control the data flow between different thread and state process and storage sequence. 
- **Alert management module** : Control when and how the program will trigger and display alerts or warning.
- **Pre-Configured instance response module**: auto execute the preset instance response code based on the user's setting when the alert module raise a alert or warning

When the program started, the main thread will start 5 sub-thread with different module as shown in the architecture diagram. 

#### 1. IT Data Manager Thread

The thread run periodic with different module to handle the IT network data communication (HMI to HMI, HMI to data base) and a IT data preprocessing module to filter the old data or None data. For each module's function 

- **Database Comm Client ** : Sqlite3 client to fetch data from the data base (Supervisory-Level HMI) or insert data to data base (Machine-Level HMIs)
- **HMI Comm Client/Serve **: A normal UDP server if the HMI is mater mode for other HMI connect to, or UDP client if the HMI is slave mode to connect to the Master HMI. 
- **IT Data Storage module ** : Data management module to store, pre-filter, combine the IT data from data base or other HMI, then send the pre-processed data to the Data mapping module in the data processing thread. It will also send the raw data to the local I/O manager thread to log the data.

#### 2.OT Data Manager Thread

The OT data manager Thread will handle the communication from HMI to all the OT controllers with multiple different OT-Comm Client and a OT data pre-processing module to process the OT data:

- **OT-Comm Clients**: Based on how many PLC the HMI will connect to and the PLC protocol, the OT data manager will create related number of OT-Comm client with the related OT protocol connectors.
- **Raw OT Data Storage and process module** : Control and filter the raw OT data in one data fetch round, fill the data in the related dictionary and send the raw data to the local I/O manager thread to log the data.

#### 3.Data Processing Thread

The main "data processing center" of the HMI program, all the data will be filtered, converted, verified and stored in this Module

- **OT Data Covert module** : convert the OT data such as the register NC NO state to True/False, 0/1 
- **Data Mapping module : ** Mapping the data to the information such memory int value to voltage value,  True/False to indicator on and off state
- **Data filter module**: filter the duplicate data or the old data. 
- **Data verify module** : Verify whether the data is under the correct range and trigger the alert based on user's configuration.
- **Data Process module** : Interact with the main thread's data control module to generate the summarized data based on the main thread data controller's request.

#### 4.UI Display Manager Thread

The thread to provide all the UI display for user and handle the user interaction such as press a button. 

- **UI Components Manager** : Work as a graphic engineer to generate all the components state show in the UI such as the value, indicator color,  animation (such as alert indicator blinking)
- **Display Refresh Manager** : the real display panel to visualized the components generate by the UI Components Manager for each frame. 
- **User Action and Event handler** : Take the user action and send to the main controller, such as when a user press the button to turn off a breaker.

#### 5.Local I/O Manager Thread

The thread to handle the I/O between the HMI program and the host computer.

- **Config loader** : Read the configuration file to init the program and change the system global setting based on the user's configuration update. 
- **Log and record generator**: Log all the data to the related log file, roll over if the log file is big (10MB), create HMI screen shot when abnormal situation appear. 
- **Global Variable module**: Control all the global variable of the program and interact with the main thread's data controller.