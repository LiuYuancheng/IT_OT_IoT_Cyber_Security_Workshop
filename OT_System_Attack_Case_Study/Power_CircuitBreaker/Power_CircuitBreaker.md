# OT Power Grid System Development

### How to Use PLC to Remote Control Circuit Breaker in Power Grid System 



**Project Design Purpose:** This project aims to use Programmable Logic Controllers (PLC) to remote monitor and control the circuit breakers in the power grid system. We will use the Schneider circuit break and PLC to introduce about the hard ware connection, then explain how to create the breaker state sense and control PLC ladder diagram. We will also explain how to figure the power system exception (such as power trip) based on the PLC contact and coil state. In the end we will also show how we simulate the whole control sequence with our power grid digital equivalent simulation system.

```
# Version:     v0.0.2
# Created:     2024/09/18
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
```

[TOC]

 

------

### Introduction

PLC are widely used in power system to remote monitor and control purpose. We will example a simple PLC remote control circuit breaker example case by using the Schneider PLC, circuit breaker, breaker position sensor and breaker remote control breaker. We will introduce the below section: 

- Physical device / hardware wire connection 
- PLC ladder logic design. 
- Power system Scada HMI circuit break monitor and control. 
- Exception or alert simulation handling. 
- Digital equivalent simulation system design.





### Hardware Connection

To build a PLC controllable circuit breaker, we need five components:  5V relay with a 48V contact, circuit breaker, breaker state sensor, the breaker control motor and the PLC.

- **5V relay with a 48V contact** : the 5V-DC relay with 48 V contact is used to take the PLC's Coil output and control the 48 V DC supply for the breaker control motor. We will use the Weidmuller 2614860000 TOP 5VDC 48VDC0.1A [Production link](https://catalog.weidmueller.com/catalog/Start.do?localeId=en&ObjectID=2614860000)
- **High Voltage AC Circuit breaker** : The AC breaker is used to control the AC power on off. We will use the Schneider Electric A9F04206 MCBs IC60N 2P, 6A C [Production link](https://www.se.com/sg/en/product/A9F04206/miniature-circuit-breaker-mcb-acti9-ic60n-2p-6a-c-curve-6000a-iec-608981-10ka-iec-609472-double-term-/)
- **breaker state sensor** : the breaker state sensor will be used to detect the position of the circuit breaker, we will use the Schneider Electric A9A26924 - Acti 9 - Auxiliary contact iOF - 1 C/O - AC/DC
- **Breaker control motor** : The breaker control motor module will accept the pLC control signal and flip on or off the circuit breaker. we will use the Schneider Electric Acti 9 - ARA auto recloser aux for iID 2P
- PLC: we will use the Schneider Electric M221 plc which support Modubus TCP to control the system. 