# Reverse Engineering to Get the Python Malware Source Code via DFIR Memory Dump

In the world of cybersecurity, understanding how to dissect and analyze malware is a critical skill—especially during Digital Forensics and Incident Response (DFIR) operations. One common scenario involves encountering malicious executables written in Python but compiled into Windows executable (EXE) files. 

In such cases, analysts often rely on memory dumps to retrieve and reverse engineer the malware’s behavior and underlying code.This article will introduce the detailed steps about how to extract a complied windows malware exe file (coded by python) from the windows memory dump data, then decompile the data to get the Python source code. The guide is structured into five key sections:

1. Creating a Python-based malware simulation Windows-OS executable program.
2. Configuring the malware victim node system for memory dump data collection.
3. Capturing the memory dump during malware execution.
4. Extracting malware data/files from the memory dump.
5. Decompiling the extracted data back into readable python source code.


We will also introduce about the tools used by finishing each section, so if you're a DFIR practitioner or a cybersecurity enthusiast you can also used them for memory forensics and Python malware analysis.

```
# Author:      Yuancheng Liu
# Created:     2025/04/06
# version:     v_0.0.1
# Copyright:   Copyright (c) 2025 LiuYuancheng
# License:     MIT License
```

[TOC]

------

### Introduction

The Digital Forensics and Incident Response (DFIR) is a cornerstone of modern cybersecurity, playing a critical role in identifying, investigating, and mitigating cyberattacks. Within DFIR, **memory forensics** has become an essential technique, allowing analysts to extract volatile evidence from system memory that might not be present on disk or network traffic. As shown in the below DFIR contents diagram. 



![](img/s_02.jpg)

Before diving into the hands-on steps, we provide essential background knowledge about DFIR and introduce the tools utilized in this project.This article falls under the *Memory Forensics* domain of DFIR and focuses on a practical reverse engineering scenario commonly used in cyber exercises and training events. Specifically, we demonstrate how to extract and recover the source code of a Python-based malware sample that was compiled into a Windows executable, using only a memory dump captured during its execution. 

#### Background Knowledge about DFIR

**Digital Forensics and Incident Response (DFIR)** is a cybersecurity discipline dedicated to understanding, responding to, and recovering from security incidents. It includes two main areas:

- **Digital forensics:** Involves the analysis of system data, user behavior, and digital evidence to uncover how an attack happened and who may be responsible.
- **Incident response:** Encompasses the strategies and processes organizations follow to detect, contain, and remediate threats in real time.

Digital forensics branches into multiple areas, including file system forensics, network forensics, log analysis, and **memory forensics**, which is the core focus of this article.

> Reference Link: https://www.crowdstrike.com/en-us/cybersecurity-101/exposure-management/digital-forensics-and-incident-response-dfir/#:~:text=Digital%20forensics%20and%20incident%20response%20(DFIR)%20is%20a%20field%20within,investigation%2C%20and%20remediation%20of%20cyberattacks.

#### Tools Used in This Project

This project utilizes multiple tools across different environments:

- **PyInstaller** (Windows): Used to compile Python scripts into standalone Windows executable files.
- **Volatility3** (Ubuntu): A powerful framework for memory forensics, used here to analyze memory dumps and extract malware-related data.
- **uncompyle6** (Ubuntu/Windows): A decompilation tool that converts Python bytecode (.pyc files) back into readable source code.

We use a Windows 11 machine to generate the malware EXE, a Windows 10 virtual machine to execute and capture memory dumps, and an Ubuntu system to perform analysis and reverse engineering.

With this foundation in place, we’ll now walk through each step of the process—from compiling the malware to recovering its source code from memory.



------

### Creating a Python-based Windows Executable

**Host machine** : Windows-11

**Tool** : PyInstaller https://pyinstaller.org/

As part of this DFIR memory forensics exercise, we need to simulate the behavior of malware running on a target victim system. To do this, we'll create a Windows executable from a Python-based malware script using **PyInstaller**, a tool that compiles Python programs into standalone executables.

In this section, we will generate an `.exe` file for a simulated backdoor trojan malware sample sourced from the following GitHub repository : https://github.com/LiuYuancheng/Python_Malwares_Repo/tree/main/src/backdoorTrojan

**Step 1: Install PyInstaller**

Use `pip` to install PyInstaller on the host Windows 11 machine:

```
pip install -U pyinstaller
```

**Step 2: Compile the Python Script into an Executable**

Navigate to the directory containing `backdoorTrojan.py`, then run the following command to generate a single executable file using the `--onefile` flag :

```
pyinstaller --onefile .\backdoorTrojan.py
```

Once the process completes, the compiled executable `backdoorTrojan.exe` will be located in the `dist` folder, as shown below:

![](img/s_03.jpg)

Then we rename the output file (e.g., to `testInstaller.exe`) and copy it to the target virtual machine where the memory dump will be collected.



------

### Configuring Windows for Memory Dump Collection

**Target Machine:** Windows 10

**Tool:** N/A (Built-in Windows settings and Registry Editor)











A memory dump is taking all the information in your device’s working memory (RAM) and creating a copy of it in your computer's hard drive. This process happens automatically when a computer crashes and right before the power turns off. To collect the memory dump file in a windows VM, the memory file will be nearly same size of your memory, we need to make sure the VM disk has enough space (Assume your VM RAM config is 16GB, then we need to make sure there will be 16GB free space in the VM disk) . 

Step 1 : Enable the Windows memory dump setting

Follow below steps to enable the windows memory dump setting

1. In **Control Panel**, select **System and Security** > **System**.
2. Select **Advanced system settings**, and then select the **Advanced** tab.
3. In the **Startup and Recovery** area, select **Settings**.
4. Make sure that **Kernel memory dump** or **Complete memory dump** is selected under **Writing Debugging Information**.
5. Restart the computer.

As shown below: 

![](img/s_04.png)

Step 2 Enable the parameters in the Registry 

Open the registry editor with Run `regedit`

![](img/s_05.png)

1. In Registry Editor, locate the following registry subkey:

   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CrashControl`

2. Right-click **CrashControl**, point to **New**, and then select **DWORD Value**.

3. Type *NMICrashDump*, and then press Enter.

4. Right-click **NMICrashDump**, and then select **Modify**.

5. In the **Value data** box, type *1*, and then select **OK**.

Then make sure the `alwayskeepmemoryDump` parameter is set to 1 as shown below:

![](img/s_06.png)



------

### Collect the memory dump file. 

**Host machine** : Windows-10

**Tool** : N.A 

After finished the configuration, we can start to run the malware and collect the memory dump file.

Then we start to run our backdoortrojan malware simulator (testInstaller.exe), when the program is running,  we need to *create a memory dump by "blue screen" kernel crash"  : 

To trigger a memory dump on a virtual machine using the keyboard, press and hold the "Ctrl" key while pressing the "Scroll Lock" (for some keyboard you need to hold the function key "Fn" to enable the Scroll Lock ) key twice; this keyboard shortcut will typically force a crash and generate a memory dump file on the VM. 

Key points to remember:

- **Shortcut:** 

  Ctrl + Scroll Lock + Scroll Lock 

- **Functionality:** This shortcut sends a specific signal to the virtual machine, essentially simulating a hardware error, which prompts the operating system to create a memory dump file. 

Then when you press the Scroll Lock twice, you will see the system crash as shown below:

![](img/s_07.png)

Don't do any thing until the system reach 100% and restart itself, then you will find the dump file `test.dmp` in the "`C:\dump`" folder as shown below:

![](img/s_08.png)



------

### Parse the memory dump to get the executed malware data. 

**Host machine** : Ubuntu

**Tool** : volatility3, https://github.com/volatilityfoundation/volatility3

Now we get the memory dump file, we can try to use the volatility3 to get all the data from the memory.

Step 1 :  Install the volatility3in host machine with pip

```
pip install volatility3
```
Step 2: Use volatility3 to find the target program's process ID Af
After we install the volatility3, we can use the vol command, use the command 
```
vol -f test.dmp windows.pslist
```
to get the target malware program's windows process ID:

![](img/s_09.png)

As we renamed the backdoor trojan to testInstaller(as shown in the below image), we can find that process tree, there are 2 process ID 3968 and 8276. As the process 8276's parend process ID (PPID) is 3968 so the init process is 3968. 

Step 3: pase the malware data from the dump file. 
Now we have confirm the process we need to focus on, we need to extract the data from the memory dump file
```
vol -f test.dmp -o output  windows.dumpfiles --pid 3968
```
Then we save the data to output folder as show below:

![](img/s_10.png)

The file `file.0xd084eb19a620.0xd084eb13d150.DataSectionObject.testInstaller.exe.dat` is the data what we need.

------

### Decompile the malware data back to source code 
**Host machine** : Ubuntu

**Tool** : 
pyinstxtractor, [https://github.com/volatilityfoundation/volatility3](https://github.com/extremecoders-re/pyinstxtractor)
uncompyle6 https://pypi.org/project/uncompyle6/

Step 1: extract the python class file  pyc from the data file.

Download the pyinstxtractor from github and copy the file.0xd084eb19a620.0xd084eb13d150.DataSectionObject.testInstaller.exe.dat with the same folder of the pyinstxtractor.py then run cmd:

```
python3 pyinstxtractor.py file.0xd084eb19a620.0xd084eb13d150.DataSectionObject.testInstaller.exe.dat 
```
we will get the pyc program as shown below:

![](img/s_11.png)

The pyinstxtractor  show the compile python version is 3.7, so we need to create a virtual environment use 3.7 to extract the files, otherwise the `PYZ-00.pyz_extracted` will be empty. as shown below:

![](img/s_12.png)



Step 2 : Decompile the python class file to source code

Find the main execution backdoor trojan program from the extract fodler:

![](img/s_13.png)



Decompile the PYC program with uncompyle6 with command 

```
uncompyle6 backdoorTrojan.pyc >> sourcode.txt
```
Then we can get the decompiled source code of the backdoor trojan as shown below:

![](img/s_14.png)

Now we can analyze the malware simulation program's activities. 



To decompile the import lib, go to the `PYZ-00.pyz_extracted` folder, if the decompile host machine's python version is different from the compile machine, the  `PYZ-00.pyz_extracted` will be empty.



------

> last edit by LiuYuancheng (liu_yuan_cheng@hotmail.com) by 11/04/2025 if you have any problem, please send me a message. 




