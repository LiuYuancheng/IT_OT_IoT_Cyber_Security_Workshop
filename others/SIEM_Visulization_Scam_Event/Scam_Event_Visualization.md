# SIEM Big Data Visualization: Dashboard for Monitoring Scam Events in Critical Infrastructure

**Project Design Purpose**:  In a Security Information and Event Management (SIEM) system, effective monitoring and visualization of scam events is crucial to detecting and responding to cyberattacks. Cybercriminals often use deceptive methods to exploit individuals or organizations, aiming to steal sensitive information, financial assets, or disrupt operations. This project seeks to develop a web plugin dashboard to help cybersecurity researchers and managers better understand the scope and impact of scam-related cyberattacks targeting critical infrastructure sectors such as `Government Services`, `InfoComm`, `Manufacturing, Energy`, `Transportation`, `Healthcare`, `Security and Emergency Services`, and `Banking and Finance`. By enabling real-time visualization of attack patterns, the dashboard will assist organizations in identifying trends, spotting anomalies, improving cybersecurity strategies, and making informed, data-driven decisions.

```
# Version:     v0.0.1
# Created:     2024/10/01
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
```

**Table of Contents**

[TOC]

------

### Introduction

This project aims to develop a dashboard that visualizes large datasets of scam threat events sourced from publicly available cybersecurity datasets. The dashboard will be an essential tool for cybersecurity researchers and managers, allowing them to analyze and understand scam incidents targeting critical infrastructure. By offering real-time visualization, it will help organizations gain insights into attack patterns, trends, and sector-specific vulnerabilities.

The dashboard will feature several key components: an `event count timeline panel`, a `scam event world heatmap`, `sector-specific line charts` displaying various scam threat types, and a `pop-up information dialog` for in-depth event breakdowns and graphical analysis.

- Types of Cybersecurity Scams Visualized: `Phishing`, `Ransomware`, `Tech Support Scams`, `Business Email Compromise (BEC)`, `Investment or Charity Scams` and `Cryptocurrency Scams`. 
- Critical Infrastructure Sectors Covered: `Government Services`, `InfoComm (Information and Communication)`, `Manufacturing-related Services`, `Energy Services (Utilities, Power)`, `Transportation Services`, `Health and Social Services`, `Security and Emergency Services`, `Banking and Finance`. 
- Visualization Methods Applied: `Heatmaps` for geographical representation of incidents, `Bar/Pie Charts` for comparing scam events by type and sector, `Geographic Maps` for scam event locations, `Timeline Graphs` for visualizing trends over time. 

The project is divided into two main sections: **Front-End Web Host** and **Back-End Database Balancer**.

- **Front-End**: The front-end is powered by an Angular web host that serves the user interface and handles HTTP requests. This allows users to interact with the dashboard, view visualizations, and explore the data.
- **Back-End**: The back-end consists of a GraphQL query system that optimizes data retrieval from the database cluster. It efficiently handles multiple user queries by balancing request loads and converting GraphQL queries into native queries, while ensuring user data permissions and access limitations are respected.

This integrated system will provide a powerful and user-friendly platform to monitor and analyze scam threats, helping to enhance cybersecurity strategies and decision-making for critical infrastructure protection.



#### Dashboard Main UI View

The dashboard layout is designed to offer an intuitive and data-driven experience, providing cybersecurity professionals with real-time insights into scam activities and their impact on critical infrastructure A preview of the Dashboard Webpage View is shown below:

![](img/s_03.gif)

The dashboard consists of five key sections, designed to provide a comprehensive view of scam threat data:

- **Total Scam Threats Timeline Chart**: Displays the total count of scam events over time, with an adjustable time unit (e.g., daily, weekly, monthly) to allow for flexible time-based analysis.
- **Scam Threats World Heatmap**: Visualizes the geographic distribution of scam sources (attackers), categorized by country, showing the intensity of scam activities across different regions.
- **Sector-Specific Scam Timeline Panel**: Compares the historical scam activity targeting different critical infrastructure sectors, with a summary overlay that highlights key trends and sector-specific insights.
- **Detailed Breakdown Pop-Up**: Provides in-depth analysis of scam events, including country-specific activity, sector targeting, campaign details, and scam types (e.g., **Email Traps**, **Extortion Tactics**, **Tech Support Scams**, **NSFW Phishing Scams**). It also includes a scannable timeline chart showing scam events for the most recent month.
- **Scam Source-Destination Relationship Graph**: Depicts the relationship between scam sources and targeted sectors or subscribers, with a filter function that allows users to rebuild the graph based on scam event count and other criteria.



------

### Scam Data Source

To gather scam event data, you can build your own database by utilizing various sources such as **Incident Reports**, **Threat Intelligence Feeds**, **Security Bulletins**, **Historical Cyberattack Data** (e.g., ransomware, phishing), as well as **User/Employee Reports of Suspicious Activities**, and **Industry-Specific Security Audits and Assessments**. Additionally, there are several free resources that provide valuable datasets for scam event research, analysis, and visualization:

| Source Name                                           | Scam Sector Covered                             | Description                                                  | Link                                                         |
| ----------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| PhishTank                                             | Banking, Government, and Information Services   | A free community-driven site where users submit and track phishing websites. | [PhishTank](https://www.phishtank.com/)                      |
| APWG (Anti-Phishing Working Group) Reports            | Banking, Government and geographic distribution | APWG provides free quarterly reports on phishing trends      | [APWG Reports](https://apwg.org/)                            |
| Have I Been Pwned (HIBP)                              | information and communication, health           | HIBP tracks breaches and scam events related to leaked user data. | [Have I Been Pwned](https://haveibeenpwned.com/)             |
| Cybercrime Tracker                                    | Energy and Transport                            | Tracks various types of cybercrime including phishing, ransomware, and command & control servers. | [Cybercrime Tracker](http://cybercrime-tracker.net/)         |
| MalShare                                              | Manufacturing, Energy, and Healthcare           | A free malware repository providing a large database of malware-related data, including ransomware and phishing kits. | [MalShare](https://malshare.com/)                            |
| IBM X-Force Exchange                                  | Government, Energy, and Banking                 | IBM's threat intelligence sharing platform that provides free access to a wide range of cybersecurity threat data. | [IBM X-Force Exchange](https://www.ibm.com/docs/en/qradar-on-cloud?topic=administration-x-force-integration) |
| Spamhaus Project                                      | Information Services and Banking                | Spamhaus provides data on spam and phishing sources across the internet. | [Spamhaus](https://www.spamhaus.org/)                        |
| CIRCL MISP (Malware Information Sharing Platform)     | Energy or Transportation                        | An open-source threat intelligence platform that aggregates and shares scam event data. | [CIRCL MISP ](https://www.bridewell.com/insights/blogs/detail/misp-open-source-threat-intelligence-platform?creative=&keyword=&matchtype=&network=x&device=c&utm_term=&utm_campaign=(CVM)_Brand+PMax&utm_source=adwords&utm_medium=ppc&hsa_acc=5928684088&hsa_cam=16617826304&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG7X__ep9uAhtFtIImaQN10sPTvDn9RlbLngMi78A1YmXJW2ZcaRooxoCo9YQAvD_BwE) |
| OpenPhish                                             | Banking and Government                          | A threat intelligence platform focused on phishing, offering both free and premium feeds. | [OpenPhish](https://openphish.com/)                          |
| CISA (Cybersecurity & Infrastructure Security Agency) | Energy, Transportation, and Government Services | The US government’s cybersecurity agency regularly publishes reports, alerts, and advisories on threats, including scams targeting critical infrastructure. | [CISA Alerts & Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) |
| Ransomwhere                                           | Manufacturing, Energy, and Healthcare.          | A crowdsourced ransomware payment tracking site.             | [Ransomwhere](https://ransomwhe.re/)                         |

These data sources provide a solid foundation for scam event tracking and analysis, enabling organizations to better monitor and understand cyber threats across critical infrastructure sectors.



------

### System/Program Design

The system is designed as an Angular plugin, programmed using `TypeScript`, with a back-end database balancer implemented in `GraphQL` and `JavaScript`. The back-end uses a `Druid database cluster` to manage and process data, alongside a data fetch module that integrates with various APIs to continuously pull scam event data from different sources. The system is flexible, allowing users to modify the data-fetching process and incorporate data from multiple sources.

The dashboard data visualization workflow is as follows:

![](img/s_04.png)

The dashboard contents 3 main part: Main Scam Analytics Dashboard, 

##### Main Scam Analytics Dashboard

The **Main Scam Analytics Dashboard** provides an overview of scam events across various critical infrastructure sectors. The interface contains several key elements:

- A **timeline chart** at the top, displaying the number of scam events by date, allowing users to track scam activity throughout the month.
- **16 small trend charts** to show the scam activity across different critical infrastructure sectors, includes: `1.Infocomm` , `2.Trade`, `3.Health and Social Services`, `4.Transportation Services`, `5.Banking and Finance`, `6.Real Estate`, `7.Construction`, `8.Government`, `9.Manufacturing`, `10.Water`, `11.Food and Beverage`, `12.Rental and Leasing`, `13.Accommodation`, `14.Land Transport`, `15.Legal` and `16.Energy`

- A **Geographic Heatmap** to visualize the distribution of scam events across various countries.

The Main Scam Analytics Dashboard is shown below: 

![](img/s_05.png)



##### Scam Event Breakdown Information Pop-Up Window

When a user clicks on any of the 16 sector-specific trend charts, a detailed breakdown of scam events is presented in a pop-up window, as shown below:

![](img/s_06.png)

The breakdown includes four types of information for the selected sector:

- A **pie chart** showing the geographic distribution of scams by country, indicating the percentage of scams occurring in each region.
- A **pie chart** breaking down the different categories of scams within the sector, such as `Email Traps`, `Extortion Tactics`, `Tech Support Scams`, and `NSFW Phishing Scams`.
- A **grid table** providing detailed descriptions of each scam category within the sector.
- A **bar chart** displaying the monthly trend of scam events.



##### Scam Source-Destination Relationship Graph

The Scam Source-Destination Relationship Graph provides a visual representation of the connections between scam event sources and their respective targets. Built using **Cytoscape**, this graph displays the flow of scam events between entities, highlighting the number of events and the type of scams involved.

The panel also includes a **filter function**, allowing users to customize the graph based on the number of scam threat events or other criteria. The graph is illustrated below:

![](img/s_07.png)

This relationship graph helps users analyze the source and target sectors, scam types, and event volumes to gain deeper insights into scam activities affecting critical infrastructure sectors.

This dashboard offers a robust visualization tool to monitor, analyze, and explore scam events, providing a powerful aid in managing cybersecurity threats across various sectors.

