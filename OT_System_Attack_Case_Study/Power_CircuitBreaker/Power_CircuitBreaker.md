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

PLC are wired used in power system to remote monitor and control purpose. We will example a simple PLC remote control circuit breaker example case by using the Schneider PLC, circuit breaker, breaker position sensor and breaker remote control breaker. The 