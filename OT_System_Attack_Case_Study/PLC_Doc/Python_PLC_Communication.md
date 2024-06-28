# Python and PLC Communication 

This article will introduce how to use Python Program to Communicate with Schneider M221 PLC or Siemens S7-1200 PLC. 

![](img/title.png)

[TOC]

------

### Communicate With Schneider M221 PLC

The Schneider Electric M221 PLC is a compact and versatile programmable logic controller designed for small to medium-sized automation projects. It is part of the Modicon M221 series with 16 IO, 7 relay outputs, known for its high performance and cost-effectiveness. The M221 PLC supports various communication protocols, including Modbus TCP/IP and serial communications, making it easy to integrate into existing systems. With its robust processing capabilities, extensive I/O options, and user-friendly programming via the SoMachine Basic software, the M221 PLC is ideal for controlling machinery, managing processes, and enhancing automation in industrial environments.

#### STEP1: Config the Schneider M221 PLC

Power up the connect the M221 in the network, use SoMachine editor to connect to the PLC unit, then config the fixed IP address and enable the Modbus communication of the PLC in the MyController > ETH1 as shown below:

![](img/ipconfig.png)

Then the program in the same subnet can connect to the PLC via the ip address and the modbus server. 



#### STEP2: Understand of Communication Protocol

