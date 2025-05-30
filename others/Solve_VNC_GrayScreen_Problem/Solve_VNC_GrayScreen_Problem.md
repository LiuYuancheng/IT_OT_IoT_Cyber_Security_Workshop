# Steps To Solve VNC "Gray Screen" Program on Ubuntu System

There are a lot of a graphical desktop-sharing system that allows users to remotely control another computer's screen, keyboard, and mouse such as TeamViewer, AnyDesk, Logmein. Some of them such as tiger VNC m tight VNC and real VNC use Virtual Network Computing protocol for peer to peer remote control. RFB (Remote Frame Buffer) protocol to transmit graphical updates and keyboard/mouse input over a network. But some times when you set up the VNC server on some of the Ubuntu system, when you remote login, you may see only a "gray screen" shows up and the mouse cursor change to a "x"  as shown below:

![](img/s_03.png)

Or some time you can see the background changed to gray color and only left one folder explore as shown below:

![](img/s_04.png)

And when you click the desktop you may got the unable to find Desktop error even the Desktop folder is shown there:  

![](img/s_05.png)

There are a lot of reason can caused this problem with the desktop environment not being correctly started or configured for the VNC session such the Missing or Misconfigured Desktop Environment (GNOME, XFCE, MATE), display index configured incorrect, Wrong or No Permissions for the VNC server or even run VNC Server as Root. 

There are a lot of solution online with different solution for solving this problem. This article will introduce the detailed steps to solve this kind of problem from the beginning, start with a clean ubuntu machine and it works event you want to run the VNC under root. The solution has been tested on Ubuntu 18, 20 and 22.



------

