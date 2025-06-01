# Steps to Solve the VNC "Gray Screen" Issue on Ubuntu Systems

Graphical desktop-sharing tools like TeamViewer, AnyDesk, and LogMeIn allow users to remotely control another computer’s screen, keyboard, and mouse. Among these, tools like TigerVNC, TightVNC, RealVNC offering cross-platform control through the VNC (Virtual Network Computing) protocol. By leveraging the Remote Frame Buffer (RFB) standard to transmit screen updates and input events, VNC enables remote desktop control. However, Ubuntu users frequently encounter a disruptive 'Gray Screen' issue when connecting via VNC—a blank, unresponsive display that halts productivity. This guide provides definitive steps to diagnose and resolve this common VNC server problem, restoring your remote desktop functionality on Ubuntu systems.

![](img/title.png)

```
Author:      Yuancheng Liu
Created:     2025/05/31
Version:     v_0.0.1
Copyright:   Copyright (c) LiuYuancheng
```

[TOC]

- [Steps to Solve the VNC "Gray Screen" Issue on Ubuntu Systems](#steps-to-solve-the-vnc--gray-screen--issue-on-ubuntu-systems)
    + [Problem Specification](#problem-specification)
    + [Detail Steps to Solve the Issue (Root Access Supported)](#detail-steps-to-solve-the-issue--root-access-supported-)
      - [Step 1: Install the XFCE Desktop Environment](#step-1--install-the-xfce-desktop-environment)
      - [Step 2: Install TightVNC and GNOME Flashback Session](#step-2--install-tightvnc-and-gnome-flashback-session)
      - [Step 3: Disable Wayland (Enable X11)](#step-3--disable-wayland--enable-x11-)
      - [Step 4: Prepare VNC Configuration Files (As Root)](#step-4--prepare-vnc-configuration-files--as-root-)
      - [Step 5: Initialize VNC and Create xstartup Script](#step-5--initialize-vnc-and-create-xstartup-script)
      - [Step 6: Create a Systemd Service to Autostart VNC](#step-6--create-a-systemd-service-to-autostart-vnc)
      - [Step 7: Reboot and Connect via VNC](#step-7--reboot-and-connect-via-vnc)
    + [Reference](#reference)

------

### Problem Specification 

When setting up a VNC server on some Ubuntu systems, users may encounter a frustrating issue: after connecting remotely, the screen displays only a gray background with a cursor that appears as a small black "X", as shown below:

![](img/s_03.png)

In other cases, the desktop background turns gray with only a single file explorer window (like Files or Nautilus) visible:

![](img/s_04.png)

And when you click the desktop you may got the unable to find Desktop error even the Desktop folder is shown there:  

![](img/s_05.png)

This issue is typically caused by problems in initializing the desktop environment during the VNC session. Common causes include:

- A missing or misconfigured desktop environment (e.g., GNOME, XFCE, or MATE)
- Incorrect display index settings in the VNC server
- Improper permissions or ownership of critical configuration files
- Running the VNC server as root, which may lead to environment conflicts

While there are many online tutorials offering various fixes, this article provides a step-by-step guide for resolving the gray screen issue, starting from a clean Ubuntu System. The solution works even when the VNC server is run as root and has been tested on Ubuntu 18.04, 20.04, and 22.04.



------

### Detail Steps to Solve the Issue (Root Access Supported)

This section provides a complete, step-by-step solution to resolve the **gray screen issue** in TightVNC on Ubuntu systems. The solution configures a lightweight XFCE desktop environment or GNOME Flashback session and enables VNC to function properly — even when running under the root user. 

 

#### Step 1: Install the XFCE Desktop Environment

XFCE is a lightweight desktop environment that works well with VNC.

```bash
sudo apt-get update
sudo apt-get install xfce4 -y
```

Also install XFCE goodies (optional tools and utilities):

```bash
sudo apt-get install xfce4-goodies
```



####  Step 2: Install TightVNC and GNOME Flashback Session

TightVNC is the VNC server used in this setup. GNOME Flashback provides a simpler session suitable for remote access.

```bash
sudo apt-get install tightvncserver -y
sudo apt-get install gnome-session-flashback -y
```

The XFCE or GNOME Flashback ensures lightweight, compatible desktops for VNC sessions.



#### Step 3: Disable Wayland (Enable X11)

Ubuntu uses Wayland by default, which is not compatible with many VNC configurations.

Edit the GDM3 configuration:

```bash
sudo nano /etc/gdm3/custom.conf
```

Uncomment or modify the following line:

```
WaylandEnable=false
```

Save and close the file. This ensures X11 is used after reboot. When Wayland is disabled, allowing VNC to operate under X11.



#### Step 4: Prepare VNC Configuration Files (As Root)

This guide configures VNC for the root user for demonstration. For normal usage, it’s recommended to configure under a regular user.

```bash
sudo mkdir -p /root/.vnc
sudo chmod 0644 /root/.vnc
```

Set VNC password:

```bash
sudo touch /root/.vnc/passwd
sudo chmod 0600 /root/.vnc/passwd
sudo bash -c 'echo "<your password>" | tightvncpasswd -f > /root/.vnc/passwd'
```



#### Step 5: Initialize VNC and Create xstartup Script

Start VNC to initialize config files:

```bash
vncserver
```

Then stop it for the next step :

```bash
vncserver -kill :1
```

Create or overwrite the `xstartup` file:

```bash
sudo touch /root/.vnc/xstartup
sudo chmod 0600 /root/.vnc/xstartup
sudo nano /root/.vnc/xstartup
```

Paste the following content:

```
#!/bin/sh
autocutsel -fork
xrdb $HOME/.Xresources
xsetroot -solid grey
export XKL_XMODMAP_DISABLE=1
export XDG_CURRENT_DESKTOP="GNOME-Flashback:Unity"
export XDG_MENU_PREFIX="gnome-flashback-"
unset DBUS_SESSION_BUS_ADDRESS
gnome-session --session=gnome-flashback-metacity --disable-acceleration-check --debug &
```

Make sure the file is executable:

```bash
chmod +x /root/.vnc/xstartup
```

The xstartup script explicitly starts the graphical session and disables DBUS conflicts.



#### Step 6: Create a Systemd Service to Autostart VNC

Create the VNC service file:

```bash
sudo nano /etc/systemd/system/tightvncserver.service
```

Add the following contents:

```
[Unit]
Description=TightVNC Server
After=syslog.target network.target

[Service]
Type=forking
User=root
ExecStartPre=-/usr/bin/tightvncserver -kill :0
ExecStart=/usr/bin/tightvncserver -geometry 1920x1080 -depth 24 :0
ExecStop=/usr/bin/tightvncserver -kill :0

[Install]
WantedBy=multi-user.target
```

Set permissions:

```bash
sudo chmod 0600 /etc/systemd/system/tightvncserver.service
```

Enable and start the service:

```bash
bashCopyEditsudo systemctl daemon-reexec
sudo systemctl enable tightvncserver
sudo systemctl start tightvncserver
```

The Systemd service ensures VNC starts automatically on boot.



#### Step 7: Reboot and Connect via VNC

Now, reboot the machine:

```bash
sudo reboot
```

After reboot, use a VNC client like **TigerVNC Viewer** or **RealVNC** to connect to:

![](img/s_07.png)

```
<your-ip-address>:5900
```

Or if using display `:1`:

```
<your-ip-address>:1
```

You should see a fully functional desktop like the following:

![](img/s_06.png)



------

### Reference

- https://hustakin.github.io/bestpractice/setup-vncserver-for-ubuntu/
- https://askubuntu.com/questions/800302/vncserver-grey-screen-ubuntu-16-04-lts
- https://bytexd.com/how-to-install-configure-vnc-server-on-ubuntu/
- https://unix.stackexchange.com/questions/118811/why-cant-i-run-gui-apps-as-root-no-protocol-specified

------

> Last edit by LiuYuancheng (liu_yuan_cheng@hotmail.com) at 01/06/2025, if you have any problem, please send me a message. 