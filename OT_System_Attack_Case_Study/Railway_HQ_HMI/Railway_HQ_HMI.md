# OT Railway System Development [03]

![](img/s_01.png)

### Implementing Different Human-Machine Interfaces (HMI) for a Land-Based Railway Cyber Range

```
# Author:      Yuancheng Liu
# Created:     2025/06/14
# Version:     v_0.0.2
# Copyright:   Copyright (c) 2025 Liu Yuancheng
```

[TOC]

------

### Introduction

In the operational technology (OT) environments,Human-Machine Interfaces (HMIs) play a critical role in bridging the complex control systems and human operators. In both real-world railway systems and cybersecurity training platforms, well-designed HMIs enhance visibility, improve safety, and enable timely decision-making. However, when designing HMIs for a **cyber range**—a simulated environment used for cybersecurity exercise, training and evaluation needs some different considerations and priorities.

This article explores the development of four different SCADA HMIs created specifically for a **Land-Based Railway Cyber Range**. These interfaces were designed not only to reflect the realism of an operational railway control system but also to serve the unique functional and pedagogical goals of a cybersecurity exercise and training environment. The article is structured into four main sections:

- **Fundamentals of SCADA HMIs** : A brief overview of SCADA systems and HMI principles background knowledge, using the railway domain as a case study example.
- **Design Differences [Real-World HMI vs Cyber Range HMI]** : A discussion of how HMI design requirements shift when the objective changes from operational control to cybersecurity simulation and education.
- **Functional Architecture of Railway Cyber Range HMIs** – A detailed introduction about how these HMIs interact with other simulated OT components in the railway system, including signaling, PLCs, and interlocking mechanisms.
- **User Interface and Functional Showcase** – A walkthrough of the developed HMI UI and usage, highlighting their unique features, use cases, and integration with the railway cyber range platform.

**Important:** Currently there is not a standard for designing HMIs specifically for cyber ranges. In this article, I want to share my idea about finding the "balance point" between the needs of **OT engineers** and **cybersecurity professionals**. The goal is to create an HMI that is intuitive and functional for OT operators performing system control tasks, while also providing the necessary visibility and context for cybersecurity engineers to detect, analyze, and respond to cyber incidents effectively. Striking this balance ensures that the HMI serves both operational usability and security monitoring purposes within the cyber range environment.



------

### Background Knowledge about HMI in ICS

Human-Machine Interfaces (HMIs) are critical components of modern industrial automation systems. Together with Supervisory Control and Data Acquisition (SCADA) systems, HMIs allow operators to monitor, visualize, and control complex physical processes. Within the 6 layers Industrial Control System (ICS) architecture, HMIs are typically positioned in:

- **Level 2 – Control Center Processing LAN** (e.g., SCADA/HMI workstation networks)
- **Level 3 – Operations Management Zone**, which handles production control and supervision (as shown below)

![](img/s_02.png)

This layered positioning ensures that HMIs have both the visibility of OT field data and the control capabilities needed for safe, efficient operations.

#### What Is an HMI program?

An **HMI** is a graphical user interface that enables human operators to interact with machines, controllers, or entire systems. In the context of railway, power, or maritime systems, HMIs are used to monitor real-time system status, send control commands, receive alarms, and visualize operational trends. The typical workflow of HMI is shown below:

![](img/s_03.png)

Key Features of HMI Program:

- **Graphical Interface**: Displays process graphics, system schematics, or animations to represent real-time operations.
- **Data Monitoring**: Allows visualization of machine states, sensor readings, alarms, and trend logs.
- **User Interaction**: Enables users to send commands, acknowledge alarms, or adjust parameters.
- **Platform Flexibility**: HMIs can run on industrial touch panels, desktop workstations, tablets, or web-based dashboards.
- **Alarm and Event Handling**: Facilitates prompt operator response to abnormal situations through visual and audible notifications.

#### HMI Communication Architecture

In a SCADA system, HMIs are typically connected to OT field devices (like PLCs, RTUs, IED or intelligent sensors) through various types of linkage, depending on the system architecture, security policy, and latency requirements. Below are three common types of HMI connection patterns:

##### 1. Direct Linkage (Integrated HMI Connection)

In this architecture, the HMI is **directly connected** to the OT controllers (e.g., PLCs in power systems or motor controllers on marine vessels). It operates within the same OT network and communicates using standard industrial protocols (e.g., Modbus, DNP3, IEC 60870-5-104, NMEA 2000, etc.). 

![](img/s_04.png)

Key features of the direct linkage: 

- Real-time data acquisition and control
- Simple architecture
- Low latency

**Use Case**: Common in systems where immediate operational feedback and control are required, such as emergency stop panels or motor control dashboards.

Master–Slave Linkage (Non-Integrated HMI Connection)



##### 2. Master-Slave linkage (Non-integrated HMI connection)

In more complex systems, a **master HMI** is directly linked to OT devices, while one or more **slave HMIs** connect to the master via a separate network. Slave HMIs receive data filtered and distributed by the master HMI andall the slave's control request will also send to master HMI first then forward to related controller based on the master HMI's setting. (The connection is shown below)

![](img/s_05.png)

Key features of the direct Master-Slave linkage : 

- Better control over access permissions
- Isolation between core control and auxiliary interfaces
- Suitable for multi-role operator environments

**Use Case**: Operation training systems, remote monitoring stations, or multi-tiered control rooms.



##### 3. Database Linkage (Non-Integrated HMI Connection)

In large SCADA environments, processed field data is often stored in centralized databases. Some of the HMIs such as the management HMI in this configuration access **historical or aggregated data** via standard IT protocols (e.g., SQL queries, RESTful APIs) rather than communicating directly with OT devices. The connection diagram is shown below:

![](img/s_06.png)

Key features of the direct Database Linkage : 

- Aggregates data from multiple systems
- Useful for analytics dashboards, reporting, and supervisory-level overviews
- Reduced OT network load

**Use Case**: High-level monitoring across multiple subsystems (e.g., energy, signaling, HVAC) in a unified dashboard.

##### 4. Hybrid Connection Models

Many modern systems implement hybrid architectures of the Direct Linkage, Master-Slave linkage  and  Database Linkage. combining different HMIs in the system for different operators to control and monitor the complex ICS system. 



------

### Design Differences: Real-World HMI vs. Cyber Range Simulated HMI

Designing a Human-Machine Interface (HMI) for a cyber range simulation requires a fundamentally different approach compared to building one for real-world OT training. Based on my experience from multiple cybersecurity exercises and feedback from end users, this section explores the key distinctions between the two types of HMI designs. While these observations are based on my personal experience and may not be 100% correct, they reflect real-world needs from both OT engineers and cybersecurity practitioners.

##### 1. Design Purpose and Usage Context

- **Real-World Training HMI** : These HMIs are designed to replicate actual industrial control systems as closely as possible. Their primary goal is to train OT operators in using the production system, so accuracy, realism, and fidelity are critical. The interface must mirror the layout, features, and behavior of the live system in production environment.

- **Cyber Range Simulated HMI** : The purpose of the cyber range HMI shifts from operation to defense of cyber attack. The HMI is tailored for cybersecurity training scenarios, helping defenders (blue teams) identify anomalies, investigate possible attacks, and practice incident response. It emphasizes observability, anomaly detection, and flexibility over realism.

##### 2. Protocols and Communication

- **Real-World Training HMI** : These HMIs typically simulate a single, vendor-specific OT protocol—such as Siemens S7Comm+ or Rockwell’s EtherNet/IP—because real-world devices from one vendor often use a unified protocol stack.
- **Cyber Range Simulated HMI** : To support red team exercises and simulate diverse attack vectors, the cyber range HMI integrates multiple open or standard protocols (e.g., IEC 60870-5-104, Modbus TCP, DNP3). This allows attackers to test various tactics across different protocol layers in a single environment.

##### 3. Information Display

- **Real-World Training HMI** : These interfaces need to be clear and show most critical information which for the operator to make decision. Only essential information is shown—such as alarms, system status, and critical sensor values—so that operators are not overwhelmed. Non-critical data (e.g., detailed PLC coil states or sensor response times) is often hidden to reduce distractions.

- **Cyber Range Simulated HMI** : These interfaces are designed to be information-rich. They display as much information as possible even the low-level data including PLC coil/contact states, communication latency, individual sensor statuses, and even abnormal signal behavior. Some alerts may be deliberately omitted or hidden to test the defender’s situational awareness and detection capabilities (e.g., discovering a MITM attack based on increased latency of PLC response).

##### 4. User Interaction Design

- **Real-World Training HMI** : A high degree of interactivity between the HMI and operator is expected. Operators are trained to manually acknowledge alarms, switch system modes, and control devices using HMI buttons, slider-bar and menus—closely replicating real-life workflows.
- **Cyber Range Simulated HMI** : In most cyber exercises, the HMI is projected on large screens without dedicated a human operators to control 24/7. As such, these HMIs are designed to be self-running or script-driven, automatically simulating operator behaviors or some response action. Manual controls are minimized or abstracted.

##### 5. UI Layout and Alert Management

- **Real-World Training HMI** : These typically feature a tabbed layout with separate views/tab page for alarms, process control, and trend monitoring and the operator need to switch between different tab to monitor and control the system. Alerts are pre-configured and follow fixed rules designed by the system integrator.
- **Cyber Range Simulated HMI** : To support continuous forensic recording, all critical information is displayed on a single screen—ensuring that nothing is missed in screen recordings. Additionally, the HMI allows customizable alert logic, often configured via external files, so blue teams can define their own detection thresholds or trigger conditions for dynamic learning scenarios.

##### 6. Logging and Forensics Support

- **Real-World Training HMI** : Logging is often limited to operational events and system states, primarily for training review or internal diagnostics.
- **Cyber Range Simulated HMI**: Logging and recording are extensive and forensic-focused. This includes: Continuous screen capture (e.g., video recording of UI), Logging of all control events, communication attempts, and OT messages, and even Packet-level network traffic capture (e.g., PCAP logs) for post-event analysis. These logs provide valuable datasets for post-exercise debriefing, attacker traceability, and blue team performance review.



#### Summary Table: Real-World vs. Cyber Range HMI Design

By recognizing and designing for these key differences, developers can create effective HMIs tailored to the needs of each environment—whether it's for day-to-day operational control or high-intensity cyber defense training. The difference compare table is shown below:

| **Aspect**              | **Real-World OT Training HMI**    | **Cyber Range Simulated HMI**                |
| ----------------------- | --------------------------------- | -------------------------------------------- |
| **Main Purpose**        | Operator skill training           | Cyber defense awareness, anomaly detection   |
| **Protocols Used**      | Single vendor-specific protocol   | Multiple open/standard protocols             |
| **Information Display** | Minimal, focused on critical data | Detailed, includes low-level system metrics  |
| **User Interaction**    | Manual interaction required       | Mostly automated or scripted behavior        |
| **UI Layout**           | Tabbed views                      | All-in-one view for continuous recording     |
| **Alert Configuration** | Fixed, pre-configured             | Customizable via config files                |
| **Logging Focus**       | Operational logs only             | Full data/event/packet logging for forensics |



------

### Functional Architecture of Railway Cyber Range HMIs

After introduced the background of HMI technologies and the design considerations of cyber range HMIs, this chapter introduces the functional architecture of the Land-Based Railway Cyber Range HMI system. In this system, four distinct HMIs were developed, each playing a specialized role in simulating the monitoring and control of key railway subsystems. These HMIs are designed to reflect both real-world OT logic and cyber range-specific features for enhanced training and incident simulation.

#### System Overview

As highlighted in the following system architecture diagram:

![](img/s_07.png)

The railway cyber range HMI architecture is composed of:

- **Three Machine-Level HMIs** located in the **Level 2 Control Center Processing LAN** for real-time monitoring and control of subsystems: HQ Signal System Monitor HMI, 
- **One Supervisory-Level HMI** located in the **Level 3 Operations Management Zone** for centralized system overview and emergency control.

The four HMI details are shown in below table:

| **HMI Name**             | **Primary Function**                         | **Connected Devices**         | **Protocol(s)**            | **Connection Type**        |
| ------------------------ | -------------------------------------------- | ----------------------------- | -------------------------- | -------------------------- |
| HQ Signal System Monitor | Train signal & sensor state monitoring       | PLC-00 to PLC-05              | Modbus-TCP, IEC61850-104   | Direct Linkage             |
| HQ Railway Block Monitor | Fixed Block ATP status, signal overload      | PLC-10, PLC-11                | Modbus-TCP                 | Direct Linkage             |
| HQ Train Control HMI     | Train status, third rail power control       | Track PLC + RTU00–RTU09       | Modbus-TCP, Siemens-S7Comm | Direct Linkage             |
| HQ Management HMI        | System overview, emergency override, logging | Other HMIs, DB, selected PLCs | SQL, IEC61850-104, TCP     | Hybrid (Direct + Database) |



#### 1. HQ Signal System Monitor HMI

The right side top HMI in the architecture diagram, provides real-time monitoring of train detection sensors, signal states, sensor-signal relationships, and PLC register/coil states.

**Connected Devices**:

- **PLC-00, PLC-01, PLC-02** (Junction/Fork Control)
- **PLC-03, PLC-04, PLC-05** (Station Signal Control)

**Connection Type**: Direct Linkage

**Protocols**: `Modbus-TCP` (for junction PLCs), `IEC61850-104` (for station PLCs)

**Connection Diagram** : 

![](img/s_09.png)

The signaling HMI will connect to 6 PLC with direct linage connection. It will connect to the railway junction and fork control PLC set (PLC-00, PLC-01, PLC-02)  via Modbus TCP and the station control PLC set (PLC-03, PLC-04, PLC-05) via IEC61850-104.The HMI also support master-slave mode connection. 



#### 2. HQ Railway Block Monitor HMI

The right side middle HMI in the architecture diagram,  displays the status of **Fixed Block ATP (Automatic Train Protection)** systems and enables **overload control** for track signals.

**Connected Devices**:

- **PLC-10, PLC-11** (Fixed Block Control)

**Connection Type**: Direct Linkage

**Protocol**: `Modbus-TCP`

**Connection Diagram:** 

![](img/s_11.png)

The block control HMI will connect to 2 PLC with direct linage connection. It will connect to railway fixed block auto train protection PLCs (PLC-10 and PLC-11) via Modbus-TCP to fetch the sensor and signal state. The HMI also provide the signal overload function for operator to handle the emergency situation.



#### 3. HQ Railway Train Control HMI

The Bottom-right of the architecture diagram, monitors **real-time train status**, including **speed**, **motor voltage/current**, and **power supply control** from the third rail.

**Connected Devices**:

- **Third Track Power Control PLC**
- **RTU00 to RTU09** (Train Onboard RTUs)

**Connection Type**: Direct Linkage

**Protocols**: `Modbus-TCP` (track control), `Siemens-S7Comm` (train RTUs)

**Connection Diagram** : 

![](img/s_10.png)

The Train Control HMI will connect to 2 PLC and 10 RTU with direct linage connection. It will connect to railway thrid track power control PLC via Modbus-TCP and the Trains RTU set (RTU00 - RTU09) via Siemens-S7Comm. 



#### 4. HQ Management HMI

The top-center HMI of the architecture diagram, provides a **holistic operational overview** of the railway network for HQ operators, including junctions, forks, trains, and stations. It also supports **emergency command override**.

**Integration Role**: Aggregates and displays information from other HMIs and system databases.

**Key Features**:

- Visualizes entire railway topology and subsystem statuses.
- Performs supervisory functions and emergency control using direct PLC communication.
- Supports **video logging** and **custom alert generation** for forensic review.

**Connection Type: Hybrid Model** 

**Connection Diagram** : 

![](img/s_12.png)

- **Inter-HMI Data Exchange**: Receives processed data from the Signal and Block HMIs via standard TCP communication.
- **Database Access**: Queries operational logs and train telemetry from a shared SCADA database using SQL.
- **Direct Control Channel**: Connects directly to selected **station PLCs via IEC61850-104** for emergency handling.



------

### Deployment and Usage of the Four Cyber Range HMIs in the Cyber Exercise

 When the **Land-Based Railway Cyber Range** are deployed and used within cyber exercises, the four cyber range HMIs will configure as shown below to simulate the real world HQ for the blue team training and system behavior analysis.

![](img/s_08.png)

As shown in the image, the four HMIs are deployed as follows:

- **One Supervisory HMI** — The **HQ Management HMI** — presented on a **main projector screen** to emulate the railway HQ system-wide control wall used by real-world operators.
- **Three Machine-Level HMIs** — the **HQ Signal System Monitor HMI**, **HQ Railway Block Control HMI**, and **HQ Railway Train Control HMI** — displayed on **smaller monitors or TVs** to replicate local subsystem terminals.

This setup provides a **layered view** of the system architecture, enabling both operational simulation and cybersecurity training in a realistic environment.

#### Role Distribution and Interaction in Exercises

The HMIs support two main types of participants in the cyber range:

- **HQ System Operators** :  Simulate normal railway control personnel. They can be scripted or manually operated to initiate standard or emergency control actions.
- **Cyber Exercise Blue Team Defenders**: Observe HMI outputs to detect cyber incidents, analyze system anomalies, and trace attacks across HMIs.

#### Functions in Cyber Exercise

HQ Management HMI (Supervisory HMI) : 

- Visualize the entire railway topology including junctions, blocks, stations, and moving trains.
- Aggregate data from machine-level HMIs.
- Serve as the **command and decision point** during cyber incidents (e.g., triggering IEC104 controls in emergencies).
- Provide **awareness** and **scenario-wide correlation** for blue team defenders.

HQ Railway Block Control HMI

- Real-time display of block power status and overload control signals.
- Visualization of communication with fixed block PLCs (via Modbus-TCP).
- Used to observe attack impact on block-based signaling or overload logic for instance response. 

HQ Signal System Monitor HMI

- Show the state of train detection sensors and signals.
- Visualize links between sensors and actuators.
- Interface with station and junction PLCs via both Modbus-TCP and IEC61850-104.
- Supports blue team investigation of signal spoofing, relay logic alteration, or sensor manipulation attacks.

HQ Railway Train Control HMI

- Monitor train speed, motor voltage, and current drawn from the 3rd rail.
- Control train-track power interface.
- Communicate with onboard RTUs using Siemens S7Comm protocol.
- Used in scenarios involving **train control hijacking**, **power manipulation**, or **anomalous telemetry injection**.



------

### User Interface and Functional Showcase

For the detailed User interface introduction, UI usage, customized alert configuration and use case to show how to detect the attack path/clue from the UI recording, I will introduce in the next article. 



------

> last edit by LiuYuancheng (liu_yuan_cheng@hotmail.com) by 20/07/2024 if you have any problem, please send me a message. 

