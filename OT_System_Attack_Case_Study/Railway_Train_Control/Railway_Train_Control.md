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

The simulated train in the land-based railway cyber range is built as a modular system comprising four interconnected subsystems. Each subsystem is mapped to physical world behaviors and enables cyber-physical interaction between the virtual environment and control logic. The 4 train sub-system are: 

- Train Power Control Subsystem
- Train Auto Pilot Control Subsystem
- Train Driving Control Subsystem
- Train Operation Information Report Subsystem

The design not only supports autonomous operation but also enables manual control, monitoring, and communication with a simulated railway SCADA network. The overall structure is illustrated in the diagram below:

![](img/s_05.png)



#### 1. Train Power Control Subsystem

This subsystem simulated the third rail electrification track infrastructure used in urban rail systems (as shown in the top part of the diagram). Each track block provides 750V DC to the train through a third rail segment, controlled by 3rd-track-side PLCs and HQ. For the train to receive power, two conditions must be met:

- The **third track block input breaker** (track-side) must be ON
- The **train’s onboard power breaker** must also be ON

These dual-breaker safety controls reflect real-world redundancy and support emergency power cut-off functionality.

**Key components:**

- **Railway Third Track Power (750V DC):** Simulated third rail providing traction DC power.
- **Third Track Block Power Control Breakers:** Controlled by the SCADA-integrated PLCs, these breakers supply power from the track to the train-3rdTrack power connection link.
-  **Train-3rdTrack power** : Link between the train and 3rd rail electrification track to transfer power to the train.
- **Train Input Power Control Breaker:** A local breaker onboard the train, operated by the emergency stop button or driver console.
- **Third Track Block Power Control PLC:** Controlled via Modbus-TCP from the HQ Train Operation HMI.

For the 3rd track power technical details please refer to this link: https://www.railway-technology.com/features/overhead-lines-vs-third-rail-how-does-rail-electrification-work/?cf-view&cf-closed.



#### 2. Train Auto Pilot Control Subsystem

This subsystem enables autonomous operation such as braking, acceleration, and responding to track signals. Two primary on train sensors guide this behavior:

- A **signal state receiver** at the train’s front detects upcoming track signals (e.g., STOP or CLEAR).
- A **front radar** monitors safety distance ahead to prevent collisions.

These sensor inputs are processed by the **onboard PLC**, which uses ladder logic to automatically control motor and brake behavior.

**Key components:**

- **Train Front Signal State Receiver:** Detects the nearest signal ahead and transmits the state to the PLC.
- **Train Front Radar:** Scans the area in front of the train for check whether obstacles or other trains in safety distance range.
- **Train Driving Control PLC:** Connect to the train motor and brake, executes logic to brake or accelerate based on sensor inputs.

Typical behaviors include:

- Signal RED / Blocked → Brake Activated, Motor Off
- Signal GREEN / Clear → Brake Released, Motor On
- Radar detects nearby train → Brake Activated to avoid collision



#### 3. Train Driving Control Subsystem

This subsystem simulates the physical mechanisms for motion, braking, and performance monitoring. It includes simulated actuators (motor and air brake) and sensors (speed, current, voltage, pressure) that work together to represent the train's dynamic state.

Manual override is available via the **on-train driver console**, allowing the operator to switch off auto-pilot and take control using throttle, brake, and other controls.

**Key components:**

- **Train Driving DC Motor & Air Brake:** Execute train physical movement and braking.
- **Train Speed & Motor RPM Meter:** Monitor real-time speed and motor RPM performance.
- **Electric Current & Voltage Meters:** Measure power (current and voltage) input from third rail track.
- **Air Brake Pressure Meter:** Measures air brake pressure ( PSI ) for braking control.
- **Train Driving Control PLC:** Central logic controller managing actuators and safety inputs.
- **Onboard RTU:** Gathers sensor data and reports it to the console and SCADA system.
- **Train Driver Console (HMI):** Interface for manual train operation, including throttle/brake control, door operation, and state monitoring.



#### 4. Train Operation Information Report Subsystem

To maintain centralized situational awareness, each train reports its operational state to the HQ control center in real time via a **wireless SCADA link**. This simulates a 5G or radio communication network, and uses the Siemens  S7Comm protocol to transmit data from the train’s RTU to the HQ Train Monitoring HMI.

**Key components:**

- **Onboard RTU:** Collects sensor data and sends it via communication link.
- **On-Train Antenna:** Simulated radio antenna linking from train to railway SCADA network.
- **Railway Train Communication Antenna:** Network endpoint receiving train telemetry and integrate in the railway SCADA network.
- **HQ Train Monitoring HMI:** Central dashboard HMI in HQ control center showing all train states, alerts, and statuses for supervisory control.

This reporting loop ensures HQ can monitor speed, power state, brake pressure, signal compliance, and emergency conditions across all trains in the network.



------

### Network and Communication Configuration

The train control system includes 3 different subnets with 5 buses. In the simulation we use 2 PLC simulation program control train in the OT train OT network. one RTU simulation program to collect the data from  physical world simulator and transfer the data to the on Train OT network and the Railway SCADA network.  The data flow sequence will be physical world simulator => PLC/RTU simulation program => related HMI program (driver console/HQ train monitor HMI)

- Electrical Signal Simulation Subnet : the green team network with UDP communication to simulate the electrical signal exchange. The VM and Bus in this subnet are: Railway Physical-world Simulator, Railway 3rd tack power switches control PLCs(PLC-06, PLC-07), On train operation control PLC (PLC-11, PLC12), On train RTU (RTU00 - RTU09), Electrical signal communication bus. 
- On Train local SCADA network : The network on-side the train to link the on train OT controllers (PLC and RTU) with the train driver console. The VM and Bus in this subnet are: On train operation control PLC (PLC-11, PLC12), On train RTU (RTU00 - RTU09), on-Train Modbus-TCP bus, on-Train S7comm bus, train driver console HMI.
- Railway SCADA network : The railway network outside the train included the 3rd rail track control PLC (wire connection ) and the train Information Report RTU to connect to the HQ train monitor HMI. The VM and Bus in this subnet are: Railway 3rd tack power switches control PLCs(PLC-06, PLC-07), railway SCADA s7Comm wireless bus, HQ Train monitoring HMI.

The network diagram is shown below: 

![](img/s_06.png)

As shown in the network diagram, there are five different buses in the system.

Electrical signal communication bus : 

- Function: Use high frequency UDP to link the OT devices (PLC, IED, RTU) and physical world components (breaker, motor, sensors) to simulate the electrical signal (such as voltage change) between physical devices and OT controllers. 
- Data Protocol : UDP (Text format, wire connection)
- Cyber exercise configuration : This bus will be isolated in green team networks, blue team and red team can not access the network. 

On-Train PLC Communication Bus

- Function : The communication bus in On-Train local SCADA network for the train driver console to read data from and send control command to the on-Train PLCs(PLC11, PLC12). 
- Data Protocol : Modbus-TCP (wire connection)
- Cyber exercise configuration : This bus will be isolated in blue team subnet, only blue team (train driver) can access this network, the red team can not attack this network.

On-Train RTU Communication bus

- Function : The communication bus in On-Train local SCADA network for the train driver console to read all the sensor and meter's data from the on-Train RTU (RTU00 - RTU09)
- Data Protocol : Siemens-S7Comm (wire connection)
- Cyber exercise configuration : This bus will be isolated in blue team subnet, only blue team (train driver) can access this network, the red team can not attack this network.

Railway 3rd rail track PLC Communication Bus

- Function : The communication bus in the Railway SCADA network for the HQ train monitoring HMI to connect to the  Railway 3rd tack power switches control PLCs(PLC-06, PLC-07) to read and control the power state. 
- Data Protocol : Modbus-TCP (wire connection)
- Cyber exercise configuration : This bus is open for the blue team and the red team to access. 

Railway SCADA s7Comm RTU Communication  bus

- Function : The communication bus in the Railway SCADA network for the on-Train RTU (RTU00 - RTU09) to report the train operation state to HQ train monitoring HMI through wireless connection
- Data Protocol : Siemens-S7Comm (wireless connection)
- Cyber exercise configuration : This bus is open for the blue team and the red team to access. 



------





------

> last edit by LiuYuancheng (liu_yuan_cheng@hotmail.com) by 04/07/2025 if you have any problem, please send me a message. 