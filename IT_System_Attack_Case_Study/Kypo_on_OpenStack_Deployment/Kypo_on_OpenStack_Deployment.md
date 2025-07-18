# How to Deploy KYPO_CRP on OpenStack-YOGA

**Design Purpose** : KYPO Cyber Range Platform (KYPO CRP) is an open-source platform for conducting cybersecurity training and exercises developed by Masaryk University. It is open source under the MIT license, which means that organizations can customize the cyber range or extend it for their needs. The KYPO is build based on Openstack and Kubernetes, it combine the function CTF-D and instance management. As the official installation manual is steamline : https://gitlab.ics.muni.cz/muni-kypo-crp/devops/kypo-crp-tf-deployment, This article will show the detailed steps of how I deploy the KYPO_CRP on the OpenStack-YoGA and detailed configuration with the possible problem you may meet and the detailed solution so you can success install and start to use it. This article includes 3 main parts: 

- Pre-config of the OpenStack : Configuration you need to do of your openstack before install the KYPO_CRP. 
- Full KYPO deployment step: The detailed step to use terraform to deploy KYPO base resources and Helm application. 
- Problem and usage: introduce how to access the platform and the solution of the problem you may meet during the deployment. 

```
# Author:      Yuancheng Liu
# Created:     2023/06/20
# Version:     v_0.1.3
# Copyright:   Copyright (c) 2025 Liu Yuancheng
```

**Table of Contents** 

[TOC]

------

### Introduction