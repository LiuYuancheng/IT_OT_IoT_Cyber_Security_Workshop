# OT Railway System Development [02]

### Simulating Simple Railway Station Train Dock and depart Auto-Control System with IEC104 PLC Simulator

**Project Design Purpose** : Building on the Virtual PLC Simulator with IEC 60870-5-104 communication (https://www.linkedin.com/pulse/python-virtual-plc-simulator-iec-60870-5-104-protocol-yuancheng-liu-bov7c) that I presented in the previous article, this project demonstrates one detailed use case about how the PLC/RTU simulator can drive a simplified railway-station automation control scenario. Our goal is to show step-by-step information about how core station hardware—train-position sensors, dock/depart signal lights, platform doors, platform emergency stops, station control room —can be modeled in software; how their interactions are orchestrated through a lean automatic-control circuit; and how the resulting logic is implemented and tested in ladder code within the IEC 104 virtual PLC. 

While real-world rail systems involve far richer safety layers and interlocks, the streamlined approach here is intentionally trimmed for education and rapid prototyping, giving engineers and students a practical sandbox for exploring OT-grade rail automation without the overhead of a full-scale installation.

```
# Version:     v_0.0.3
# Created:     2025/05/18
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
```

**Table of Contents**

[TOC]



------

### Introduction

This article is part of the Land Based Railway IT-OT Cyber Range System's program design wiki,  it presents a detailed walkthrough of how the Virtual IEC 60870-5-104 PLC Simulator is applied within the OT environment of Land-Based Railway IT-OT Cyber Range System I developed, specifically for monitoring and controlling the railway stations in the system. The system operates in both automatic and manual modes, covering two key functional domains:

- **Station Track Control**: Utilizing position sensors and signal logic to control train braking and acceleration, this subsystem ensures accurate train docking and safe departure guiding procedures.
- **Station Platform Control**: Managing the synchronized operation of train and platform doors, emergency stop functions, and manual override controls from the station control room.

To provide a comprehensive understanding of this simulation, the article is structured into four main sections:

- **Background Knowledge** – A brief overview of the Land-Based Railway IT-OT Cyber Range System, with a focus on the station control segment within the overall architecture.
- **Station Physical Components Simulation** – Modeling key simulated physical elements of the station such as trains position sensors, trains dock/depart signals, platform safety doors, emergency buttons, and manual control room console interfaces.
- **Platform Automatic Control Circuit Design** – Developing different control circuits that govern automatic train docking and departure sequences, platform safety door control. 
- **PLC Ladder Logic Implementation** – Programming the control logic using the IEC 60870-5-104 virtual PLC simulator to realize the station track, trains and platform automation control workflow.

If you are interested about how virtualized OT components can be integrated into rail system scenarios for training, testing, and prototyping purposes and get more information about the Land-Based Railway IT-OT Cyber Range, this is another article about how to use ModBus-TCP PLC to Implement Land Based Railway Track Fixed Block Signaling OT System: https://www.linkedin.com/pulse/use-plc-implement-land-based-railway-track-fixed-block-yuancheng-liu-saaec/?trackingId=NuOghXz8rui9f2Z4%2F5RQEQ%3D%3D



------

### Background Knowledge

The Land Based Railway IT-OT System Cyber Security Test Platform is a miniature cyber range capable of simulating the land-based railway system’s IT-OT environment. It will provide a simplified and straightforward digital-twin style Operational Technology (OT) environments emulation solution for the railway track signaling systems, train ATC and ATP system and station control system. It will also provide a customizable Information Technology (IT) environment to simulate a normal company corporate network with various users. 

The system will offer several different modules to simulate Level 0 (Physical Process Field I/O device) to Level 5 (Internet DMZ Zone) of an IT-OT environment. In this article will will introduce the station control sub system which highlight in the system architecture diagram as shown below:

![](img/s_03.png)

From the architecture view, the station control system covers 3 level of OT environment with different program implementation. 

- In the Physical Process field I/O device, the physical world simulator program will use software generate the electrical signal which generate from different sensors such as the distance echo sensor to detect the trains position in the station, then simulate the control electrical signal such as the train stop/brake/start move sgianl, the platform door driving motor on/off signal. So simulate all the physcial device's input/output to the OT device. 
- In the OT system Controller LAN level, we will use the PLC simulator I developped to pick up all the simulated electrical signal generated from the  Physical Process field I/O device level as the real world PLC do. Then in PLC I will setup different control logic to control the related station's track and platform's components to achieve the automatic control which same as the real world. 
- In the Control Center/Room Processing Lan level, I will create the HMI (human machine interface) and control console which use the OT protocol to communicate to the PLC to implement the system real time monitoring and manually overload control. 











------

> last edit by LiuYuancheng (liu_yuan_cheng@hotmail.com) by 22/05/2025 if you have any problem, please send me a message. 

