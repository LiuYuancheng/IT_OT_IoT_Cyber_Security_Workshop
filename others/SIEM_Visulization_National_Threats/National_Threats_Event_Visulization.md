# SIEM Big Data Visualization [02]

### Dashboard for Summarizing SG National Cyber Threads in Critical Infrastructure

**Program Design Purpose**: 

The purpose of this program is to develop a comprehensive angular web dashboard plugin for a Security Information and Event Management (SIEM) system, focusing on the effective monitoring, categorization, summarization, and visualization of cyber threat events targeting Singapore's critical infrastructure. This dashboard will provide researchers and security managers with a clear, concise view of national cybersecurity threats, enabling them to quickly detect and respond to potential cybercriminal activities and Advanced Persistent Threats (APTs) within a short timeframe.

Key features include visual representations of total event counts over time, identification of top-N threats, actors, and affected sectors, as well as categorization of threat actors across eight critical service sectors: `Government Service`, `InfoComm`, `Manufacturing-Related Service`, `Energy Service`, `Transportation Service`, `Health and Social Services`, `Security and Emergency Services`, and `Banking and Finance Service`. This tool will facilitate a better understanding of cybersecurity threats and help prioritize mitigation strategies across different sectors.

```
# Version:     v0.0.2
# Created:     2024/10/18
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
```

**Table of Contents**

[TOC]

------

### Project Introduction

This project aims to develop a comprehensive dashboard plugin that visualizes large datasets of Singapore national cyber threat events, sourced from publicly available cybersecurity datasets. The dashboard is designed to offer real-time insights and an overview of cyber threats impacting various critical infrastructure sectors in Singapore. By leveraging data from trusted sources such as the Singapore Cyber Security Agency (CSA) Annual Cybersecurity Report and SingCERT (Singapore Computer Emergency Response Team) advisories, the dashboard provides a centralized view of national cyber threat activities.

The Singapore National Cyber Threat Dashboard Plugin is a vital tool for enhancing situational awareness of the cybersecurity landscape within Singapore’s critical infrastructure sectors. By offering a range of intuitive visualizations and real-time data, the dashboard aids in early threat detection, trend analysis, and informed decision-making. It bridges the gap between raw data and actionable insights, empowering researchers, security professionals, and policy makers to mitigate risks and improve national cybersecurity defenses.

#### Dashboard Structure

The dashboard is organized into a grid structure, providing a clear and user-friendly interface for visualizing key information. Below is the layout of the dashboard:

| **Dashboard Title**                                  |                                                         |                                                     |                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------ |
| Total Threat Count Line-Area High-Chart              |                                                         |                                                     |                                                  |
| Top-N Threat Names Word Cloud High-Chart (Count)     | Top-N Threat Actors Pie High-Chart (Percentage)         | Top-N Threat Sectors Pie High-Chart (Percentage)    |                                                  |
| Sector Line-Area High-Chart: GOVERNMENT              | Sector Line-Area High-Chart: INFOCOMM                   | Sector Line-Area High-Chart: MANUFACTURING          | Sector Line-Area High-Chart: ENERGY              |
| Sector Line-Area High-Chart: TRANSPORTATION SERVICES | Sector Line-Area High-Chart: HEALTH AND SOCIAL SERVICES | Sector Line-Area High-Chart: SECURITY AND EMERGENCY | Sector Line-Area High-Chart: BANKING AND FINANCE |

Key visual elements include:

- **Total Threats Count**: A line-area chart depicting the overall count of detected threats over a specific period.
- **Top-N Threat Names**: A word cloud chart highlighting the most frequently detected threat names.
- **Top-N Threat Actors and Sectors**: Pie charts illustrating the distribution of threats by actors and affected sectors.
- **Sector-Specific Analysis**: Individual line-area charts for each critical sector, offering a detailed view of threat trends and activities in specific areas such as Government, InfoComm, Manufacturing, Energy, Transportation, Health and Social Services, Security and Emergency, and Banking and Finance.

#### Dashboard UI View 

The dashboard is designed with three main sections, providing a clear and intuitive way to visualize national cyber threat data. The dashboard view is shown below:

![](img/threatsDashboard.gif)

- **Total Threats Count Timeline**: This section displays a timeline chart showing the total number of detected threats, sorted by timestamp. Users can view data aggregated by day or hour, helping them track trends and spikes in cyber activity over time.
- **Top-N Threats Percentage Display**: This pane presents a summary of the most prevalent threats, categorized by threat name, actor, and affected sector. The display is configurable, allowing users to adjust the parameters based on their specific needs, such as viewing the top threats by name, key actors, or targeted sectors.
- **Sector-Specific Threat Line Charts**: This section offers line charts that categorize threat events by service type (e.g., Government, Energy, Health). Users can view trends sorted by day, which helps in identifying which sectors are most affected and how threat patterns vary across different actor service types.

The dashboard also provides interactive features: when a user clicks on data within the Top-N Threats pane or any sector panel, a detailed timeline dialog will pop up, offering an in-depth view of the selected threat information, as shown in the example image above. This functionality allows users to drill down into specific data points, enhancing their ability to analyze and respond to threats effectively.

#### Project Architecture

The project consists of two main components: the **Front-End Web Host** and the **Back-End Database Balancer**.

##### Front-End: Angular Web Host Program

- The front-end is built using Angular, providing an interactive web-based interface.
- It handles user HTTP(S) requests and delivers webpages for viewing and interacting with the dashboard.
- Users can customize and filter data views based on specific time periods, sectors, or threat types, making it easier to pinpoint relevant information.

##### Back-End: GraphQL Query Program

- The back-end is powered by a GraphQL query engine designed to optimize data fetching for multiple concurrent users.
- It efficiently manages requests by queuing and filtering based on user data permissions and access limitations, ensuring secure and scalable data retrieval.
- The system converts GraphQL queries into native database queries, pulling data from a database cluster to serve up-to-date, accurate information.

The dashboard is equipped with various data visualizations that summarize and categorize threats, allowing security professionals, researchers, and policy makers to identify trends, monitor real-time threat events, and enhance their understanding of Singapore's cybersecurity landscape.



------

