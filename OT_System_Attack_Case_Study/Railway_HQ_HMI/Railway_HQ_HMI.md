# OT Railway System Development [03]

![](img/s_02.png)

### Implementing Different Human-Machine Interfaces (HMI) for a Land-Based Railway Cyber Range

------

### Introduction

In the operational technology (OT) environments,Human-Machine Interfaces (HMIs) play a critical role in bridging the complex control systems and human operators. In both real-world railway systems and cybersecurity training platforms, well-designed HMIs enhance visibility, improve safety, and enable timely decision-making. However, when designing HMIs for a **cyber range**—a simulated environment used for cybersecurity exercise, training and evaluation needs some different considerations and priorities.

This article explores the development of four different SCADA HMIs created specifically for a **Land-Based Railway Cyber Range**. These interfaces were designed not only to reflect the realism of an operational railway control system but also to serve the unique functional and pedagogical goals of a cybersecurity exercise and training environment. The article is structured into four main sections:

- **Fundamentals of SCADA HMIs** : A brief overview of SCADA systems and HMI principles background knowledge, using the railway domain as a concrete example.
- **Design Differences [Real-World HMI vs Cyber Range HMI]** : A discussion of how HMI design requirements shift when the objective changes from operational control to cybersecurity simulation and education.
- **Functional Architecture of Railway Cyber Range HMIs** – A detailed introduction about how these HMIs interact with other simulated OT components in the railway system, including signaling, PLCs, and interlocking mechanisms.
- **User Interface and Functional Showcase** – A walkthrough of the developed HMI UI and usage, highlighting their unique features, use cases, and integration with the railway cyber range platform.

**Important:** Currently there is not a standard for designing HMIs specifically for cyber ranges. In this article, I want to share my idea about finding the "balance point" between the needs of **OT engineers** and **cybersecurity professionals**. The goal is to create an HMI that is intuitive and functional for OT operators performing system control tasks, while also providing the necessary visibility and context for cybersecurity engineers to detect, analyze, and respond to cyber incidents effectively. Striking this balance ensures that the HMI serves both operational usability and security monitoring purposes within the cyber range environment.



------

### 

Background knowledge about HMI

HMI (Human-Machine Interface) and SCADA (Supervisory Control and Data Acquisition) are crucial in industrial automation, working together to enable operators to monitor and control processes. HMI acts as the user interface, providing operators with real-time data and control over machinery, while SCADA collects, analyzes, and displays data from various devices and systems, enabling remote monitoring and control. The workflow of HMI is shown below:

![](img/s_03.png)

HMI (Human-Machine Interface) key feature:

- HMI is the user interface that allows operators to interact with machines or systems. 
- It provides a graphical representation of the process, enabling operators to monitor equipment, view data trends, and make adjustments. 
- HMIs can be accessed through dedicated screens, mobile devices, or any PC connected to the control network via a web browser. 
- HMIs can show information like machine status, level indicators, and alarm

**HMI Connection Types** 

As shown in the work flow diagram the HMI will be part of the SCADA network and connect with the OT field controllers with different OT protocol, but actually there are several different HMI connection.

**Direct linkage (Integrated HMI connection)**

The HMI is connect to the OT controller (such as PLC in power ) or OT Bus (such NMEA2000 bus motor) or OT wireless receiver (such AIS on ship pilot system) directly, the HMI will be in the same network with the OT controllers to read data and set command to the OT field device directly. This connection use standard OT protocol  

**Master-Slave linkage (Non-integrated HMI connection)**

Some system will provide the master-slave linkage connect for limit the control and data access, in this situation, there will be a master HMI connect to the OT controllers directly as master HMI, then other HMIs will connect to the master HMI wire another network, the data distributed to the slave HMI will be decided by the master HMI and all the slave's control request will also send to master HMI first then forward to related controller based on the master HMI's setting.  This connection normally use the vendor's own customized protocol.

**Data Base linkage (Non-integrated HMI connection)**

In a SCADA system there will be some data base to store the processed OT information and some OT controller will also linked to data base to fetch the processed data to executed the related control process. Some HMI will  linked to these data base with normal IT protocol for data visualization and control. This type of connection normally use the IT protocol such as sql request. 

The HMI can also use mixed connection to connect to both the OT device and data base to 