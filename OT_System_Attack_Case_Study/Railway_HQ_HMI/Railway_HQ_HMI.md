# OT Railway System Development [03]

![](img/s_02.png)

### Implementing Different Human-Machine Interfaces (HMI) for a Land-Based Railway Cyber Range

**Project Design Purpose** : 

In the operational technology (OT) environments,Human-Machine Interfaces (HMIs) play a critical role in bridging the complex control systems and human operators. In both real-world railway systems and cybersecurity training platforms, well-designed HMIs enhance visibility, improve safety, and enable timely decision-making. However, when designing HMIs for a **cyber range**—a simulated environment used for cybersecurity exercise, training and evaluation needs some different considerations and priorities.

This article explores the development of four different SCADA HMIs created specifically for a **Land-Based Railway Cyber Range**. These interfaces were designed not only to reflect the realism of an operational railway control system but also to serve the unique functional and pedagogical goals of a cybersecurity exercise and training environment. The article is structured into four main sections:

- **Fundamentals of SCADA HMIs** : A brief overview of SCADA systems and HMI principles background knowledge, using the railway domain as a concrete example.
- **Design Differences [Real-World HMI vs Cyber Range HMI]** : A discussion of how HMI design requirements shift when the objective changes from operational control to cybersecurity simulation and education.
- **Functional Architecture of Railway Cyber Range HMIs** – A detailed introduction about how these HMIs interact with other simulated OT components in the railway system, including signaling, PLCs, and interlocking mechanisms.
- **User Interface and Functional Showcase** – A walkthrough of the developed HMI UI and usage, highlighting their unique features, use cases, and integration with the railway cyber range platform.

**Important:** Currently there is not a standard for designing HMIs specifically for cyber ranges. In this article, I want to share my idea about finding the "balance point" between the needs of **OT engineers** and **cybersecurity professionals**. The goal is to create an HMI that is intuitive and functional for OT operators performing system control tasks, while also providing the necessary visibility and context for cybersecurity engineers to detect, analyze, and respond to cyber incidents effectively. Striking this balance ensures that the HMI serves both operational usability and security monitoring purposes within the cyber range environment.



------

### Introduction 





Background knowledge about HMI

HMI (Human-Machine Interface) and SCADA (Supervisory Control and Data Acquisition) are crucial in industrial automation, working together to enable operators to monitor and control processes. HMI acts as the user interface, providing operators with real-time data and control over machinery, while SCADA collects, analyzes, and displays data from various devices and systems, enabling remote monitoring and control. 

HMI (Human-Machine Interface):

- HMI is the user interface that allows operators to interact with machines or systems. 
- It provides a graphical representation of the process, enabling operators to monitor equipment, view data trends, and make adjustments. 
- HMIs can be accessed through dedicated screens, mobile devices, or any PC connected to the control network via a web browser. 
- HMIs can show information like machine status, level indicators, and alarm