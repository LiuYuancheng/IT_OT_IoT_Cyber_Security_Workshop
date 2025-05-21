# OT Railway System Development [02]

### Simulating Simple Railway Station Train Dock and depart Auto-Control System with IEC104 PLC Simulator

**Project Design Purpose** : In the previous article https://www.linkedin.com/pulse/python-virtual-plc-simulator-iec-60870-5-104-protocol-yuancheng-liu-bov7c, I introduced the Virtual PLC Simulator with IEC-60870-5-104 Communication Protocol, in this article I will introduce how we use the IEC104 PLC simulator to implement the railway trains station's train automatic docking and departure control logic in the land based railway system. This article will introduce 3 main part:

Station Physical Components Simulation : The physical components such as the station train position sensor, train dock and depart signals, platform doors, emergency control button. 

Platform automatic control circuit design : The circuit design to implement train auto control in the station. 

PLC ladder logic implementation : use the IEC104 virtual PLC simulator to implement the platform automatic control .

> **Important:** The Real-world station control system are much more complex than what we introduced in the article. This project simplifies the general operation logic for training purposes only.

```
# Version:     v_0.0.3
# Created:     2025/05/18
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
```

**Table of Contents**

[TOC]

