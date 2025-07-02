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

### Overview of the Train Simulation System

The train simulation system is one of the core components of the land-based railway cyber range. It represents the physical-world operation of trains in a simplified and controlled environment designed for cybersecurity training and system behavior analysis. Within this simulation, ten autonomous trains are visualized as sequences of 5 to 7 rectangles each (based on the train length user configured), moving along three interconnected tracks at speeds ranging from 0 to 20 pixels per second (approximate visual simulation speed). The trains are high lighted on the physical world simulator screen shot as shown below :

![](img/s_03.png)

Each train is a self-contained unit that interacts with its environment—including track signals, power systems, and sensors—while being monitored and controlled through two main interfaces as shown below:

![](img/s_02.png)

- **On-Train Driver Console** (local control HMI)
- **HQ Train Monitoring HMI** (central supervisory interface)

#### Key Features of Each Simulated Train 

Each Train will interact with other components on the physical world simulator with below key features : 

- **3rd Track Power Interaction** : Each train relies on the availability of power from a simulated third track power system. If third track power is lost, the train transitions to a powerless, stationary state.
- **Sensor and Signal Response** : The train will interact with the train detect sensors, it will trigger the sensor when it pass through the sensor position. Trains are capable of detecting and reacting to track signals. If a signal ahead indicates a "block" condition, the train will automatically reduce speed and come to a stop before the signal.
- **Dynamic Parameter Generation** : Each train continuously generates telemetry data, including: Speed (km/h), Motor input current (A), Motor voltage (V), Position in block zones, Throttle and brake status. 
- **Internal Control Network** : Every train hosts an onboard OT control network, integrating a Programmable Logic Controller (PLC) to control the train, it also have one RTU to remote connect to the railway SCADA network. This allows both local (driver) and remote (HQ) control.

#### Operation States of the Simulated Train

As depicted in the image below, each train transitions through four operational scenarios depending on its power state, control inputs, and environmental conditions. The train will have 4 different operation states as shown below picture : 

![](img/s_04.png)

| Operation scenario | Visual Indicator      | Scenario description                                         |
| ------------------ | --------------------- | ------------------------------------------------------------ |
| **Scenario 1**     | 🔴 Red + Gray Blinking | **Power OFF**: Train is not powered. Speed = 0 km/h, Current = 0A. Occurs when third rail power is lost or driver turns off the train motor input breaker. |
| **Scenario 2**     | 🟠 Orange              | **Low-Speed / Braking State**: Train is powered, but moving slowly (0–20 km/h). Current draw is between 10–20A. Typically seen during station docking or braking before a red signal. |
| **Scenario 3**     | 🟢 Green               | **Running State**: Train is fully operational and in transit, moving between 56–90 km/h. Current draw is high (140–180A), brake is off, throttle is active. |
| **Scenario 4**     | 🔴 Red + ⚠️ Alert Icon  | **Emergency / Fault State**: Triggered by failures, system errors, or accident simulations. Power is cut, train stops immediately (0 km/h, 0A), and alert status is raised. |

These operational states help replicate realistic behaviors in response to faults, signal changes, or cyber-induced disturbances, providing a comprehensive platform for evaluating both safety mechanisms and cybersecurity resilience in railway systems.



------

### System Design of the Simulated Train

For the simulated train, we implement the components as shown below diagram with 4 different sub system: 

- Trains power control sub-system
- Trains auto pilot control sub-system 
- Trains driving control sub-system 
- Trains operation information report sub-system

![](img/s_05.png)

#### Trains power Control subsystem

I simulate the third rail track power supply solution for providing the power to trains, for the 3rd track power please refer to this link: https://www.railway-technology.com/features/overhead-lines-vs-third-rail-how-does-rail-electrification-work/?cf-view&cf-closed. Each block of the third track will provide 750VDC to the linked train to that specific block, each block's power is controlled by the third track block power control PLC which linked to HQ, so if HQ detected any emergency situation, it can cut off the power supply of the third track. On the train side there is another power input breaker to control the power from the 3rd track power to train link, this breaker can be cut off by the on-train's emergency stop button. So need both the 3rd track power breaker and the train input power breaker on then the train will get power.

The main components of the trains power system:

- Third rail track power : The power link next to the track to provide 750V-DC power for the trains. 
- Third track block power control PLC: PLC in the railway SCADA network all the HQ train operation HMI to control the thrid track's power state. 
- Third track power block Input control breakers : Breaker on track control by third track block power control PLC to provide power from 3rd rail track to the track-train power link. 
- Train input power control breaker: Breakers on train control the power from  track-train power link to the train's internal circuit. 

#### Trains auto pilot control sub-system 

I simulate the train auto pilot control system on the train, the train will auto brake, accelerate, dock and departure based on the signals along the track. at the train head, there is one train front signal state receiver to receive the signal instruction in front the train under a distance. The receiver will linked to the train driving PLC, if the train front receiver receive the stop / front block lock signal, it will turn off the motor and turn on the air break to decrease the speed and stop, if it receive the front clear / lock release signal, it will turn on the motor and release the break to make the train accelerate. The Train also have one front radar for train detection, it will scan the train front safety distance to avoid the collision, if the radar detect a train in front less than the safety distance, it will auto trigger the brake procedure of the train.

The main components of the Trains auto pilot control sub-system: 

- Train front radar : A Rada sensor scan the safety distance (pixel area in the physical world simulation) to detect whether there is a train in front less that the safety distance, then send the information to Train driving control PLC. 
- Train front signal state receiver : receiver to get the front nearest railway tracks' signal state and send the information to train driver PLC.
- Train driving control PLC : The PLC will auto-control ladder logic to control the train motor and air brake based on the front radar and signal state receiver's feed back. 

#### Trains driving control sub-system 