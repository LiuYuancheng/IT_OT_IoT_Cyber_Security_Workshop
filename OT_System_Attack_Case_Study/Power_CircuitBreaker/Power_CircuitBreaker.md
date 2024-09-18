# OT Power Grid System Development

### How to Use PLC to Remote Control Circuit Breaker in Power Grid System 





**Project Design Purpose:**
The goal of this project is to demonstrate how to utilize Programmable Logic Controllers (PLC) to remotely monitor and control circuit breakers within a power grid system. Using a Schneider circuit breaker and PLC hardware, the project will cover the physical hardware connections and provide a step-by-step guide for designing a PLC ladder diagram  to sense and control the breaker states. Additionally, the project will explain how to detect power system anomalies, such as power trips, based on the states of PLC contacts and coils from the power system control SCADA HMI. Finally, a digital power grid digital equivalent  simulation will be used to model and simulate the entire control sequence for the people who don't have the hardware.

```
# Version:     v0.0.2
# Created:     2024/09/18
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
```

[TOC]

 

------

### Introduction

Programmable Logic Controllers (PLC) are essential in power systems for remote monitoring and control of key equipment like circuit breakers. This project focuses on a practical example of using a Schneider PLC to remotely control a circuit breaker, along with integrating sensors and remote control mechanisms. The project will guide through:

- **Physical device/hardware connections**: Setting up wiring between the PLC, circuit breaker, position sensors, and control devices.
- **PLC ladder logic design**: Developing the control logic to manage breaker states and automate operations.
- **SCADA HMI integration**: Using a power system SCADA interface to monitor and control the circuit breaker remotely.
- **Exception and alert handling**: Simulating and responding to anomalies such as power trips.
- **Digital equivalent system simulation**: Designing a digital twin of the power grid to simulate and validate the entire control process.

For the  digital equivalent part, two subprojects will also be used for this system to simulate the OT device and the power grid control sequence:

- **Python Virtual PLC & RTU Simulator**: A tool to simulate the PLC devices used in the system.
- **Power Grid Simulation System**: A simulation platform for emulating physical electrical devices and providing SCADA HMI functionalities for monitoring and control.

The real power system is more complex than what we introduced, this comprehensive project will demonstrate the main idea how PLCs are used in modern power grids for safe, efficient, and reliable remote control.



------

### Physical Device Connection

To build a PLC-controlled circuit breaker system, we will need five key components: a 5V relay with 48V contacts, a circuit breaker, a breaker state sensor, a breaker control motor, and the PLC.(As shown below)

![](img/s_03.png)

- **5V Relay with 48V Contact**: This relay will interface with the PLC's 5V coil output to control the 48V DC supply for the breaker control motor. For this, we will use the `Weidmuller 2614860000 TOP 5VDC 48VDC 0.1A relay`. [Product link](https://catalog.weidmueller.com/catalog/Start.do?localeId=en&ObjectID=2614860000)
- **High Voltage AC Circuit Breaker**: The AC circuit breaker will be responsible for controlling the on/off status of the AC power. We will use the `Schneider Electric A9F04206 MCB IC60N 2P, 6A C`. [Product link](https://www.se.com/sg/en/product/A9F04206/miniature-circuit-breaker-mcb-acti9-ic60n-2p-6a-c-curve-6000a-iec-608981-10ka-iec-609472-double-term-/)
- **Breaker State Sensor**: This sensor detects the position of the circuit breaker (whether it's open or closed). We will use the `Schneider Electric A9A26924 Acti 9 Auxiliary contact iOF - 1 C/O - AC/DC`. [Product link](Schneider Electric A9A26924 Acti 9 Auxiliary contact iOF - 1 C/O - AC/DC)
- **Breaker Control Motor**: This motor module receives control signals from the PLC and operates the circuit breaker, switching it on or off. For this, we will use the `Schneider Electric Acti 9 ARA auto-recloser auxiliary module for iID 2P`. [Product link](https://www.se.com/sg/en/product/A9C70342/acti-9-ara-auto-recloser-aux-for-iid-2p-1-prog/)
- **Programmable Logic Controller (PLC)**: The `Schneider Electric Modicon M221 PLC`, which supports Modbus TCP, will be used to control the entire system. [Product link](https://www.se.com/sg/en/product-range/62128-logic-controller-modicon-m221/#products)

The hardware connection diagram is illustrated in the image below.

![](img/s_04.png)

Since the `Schneider Electric Acti 9 ARA auto-recloser motor` operates at 48V, we need to use the 5V relay with 48V contacts to bridge the PLC’s 5V output coil with the 48V power supply, enabling the motor to flip the breaker on or off. The breaker state sensor can directly connect to the PLC's 5V input. However, if a 48V PLC extension module, such as the SR2D201BD, is used, the relay and sensor connections can be linked directly to the breaker sensor and control motor, bypassing the 5V relay configuration.