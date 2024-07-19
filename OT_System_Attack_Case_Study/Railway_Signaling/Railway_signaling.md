# How to Use PLC to Implement Land Based Railway Track Fixed Block Signaling System

**Project design purpose**: We want to use PLC with sensor and signals to implement the operation of railway track fixed blocking signaling automated control system in the digital equivalent system or railway system module to show the logic of track fixed blocking ATC(Automatic Train Control) mechanism for training. 

> Important: The real world railway Automatic Train Control mechanism Automatic Train Protection(ATP) and Automatic Train Operation(ATO) are much more complex, we just simplified the general operation logic for OT training.

```
# Version:     v0.1.3
# Created:     2024/07/18
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
```

[TOC]

------

### Introduction

This document will show how to implement train fix blocking  Automatic Train Protection and Operation mechanism in a railway track digital simulation system. The implement includes 3 sub projects

1. Railway signaling system physical world simulator. 
2. PLC simulator project.
3. Railway block control HMI.  

#### Introduction of Fixed Blocking System

The track fixed blocking system is a fundamental method used in railway signaling to ensure safe and efficient train operations. This system divides the railway track into sections known as "blocks." Only one train is allowed in each block at any given time, preventing collisions and ensuring a safe distance between trains.

**Key Features of Track Fixed Blocking System:**

1. **Division into Blocks:** The railway track is divided into fixed segments or blocks, each equipped with signals.
2. **Signals:** Each block has entry and exit signals that control train movements. These signals indicate whether the block ahead is occupied or free.
3. **Train Detection:** Various technologies like track circuits, axle counters, or radio systems detect the presence of trains within a block.
4. **Safety:** By ensuring only one train per block, the system prevents collisions and allows safe operation, even in cases of signal failure or human error.
5. **Manual or Automatic Control:** Signals can be controlled manually by signal operators or automatically by computer-based interlocking systems.

The track fixed blocking system is a reliable and straightforward method for managing train traffic, providing the foundational safety mechanism for railways around the world.

> Reference: 

https://www.linkedin.com/pulse/moving-block-vs-fixed-signalling-which-better-naeem-ali/

Link: https://www.sgtrains.com/technology-signalling.html#atc





#### System Design



#### Physical World Simulation Design

To implement the fixed blocking, we need trackside ATC and trainborne ATC. There are several level of ATC such as shown in the European Rail Traffic Management System (ERTMS):

![](img/s_05.png)

Reference: https://medium.com/@POST_UK/moving-block-signalling-b9b0b9f498c2

In our simulation program, we will simplified the design and implement two elements to railway signaling:

- **Train detection** : Which recognizes when a section of track is occupied by a train In the 2D physical world simulation program, we will add the "sensor" to do the pixel detection of the moving train on the track.
- **Movement authority**: which gives a train permission to move to a particular location on the track. The train will receive the block entrance signal's pixel color to identify whether it is allowed to move into the block. 

As shown below, we match the fixed block :

![](img/s_06.png)

**Train detection Sensor**: in the 2D simulator, along the track each interval there will be a train detection sensor (small grey box), when a train (green rectangle) move over the sensor, the sensor will change to blue color and generate the simulated voltage change message. Sensor color code:

- Green: no train is detected, generate sensor "voltage low" message to block controller input pin.
- Blue: train is passing the sensor, generate sensor "voltage high" message to block controller input pin.

**Block Control Signal**: In the 2D simulator, next to the track near to each sensor, there will be a signal (big red/green box) controlled by the fixed blocking controller. The train will keep detection the front area (50 pixel), if it detect a signal is red, the train will brake to reduce the speed and stop before the signal. If the train detect the signal green color, it will pass through the signal area to enter the block.

- Red: Block controller output voltage high, track block after signal is locked and trains have no permission to move in the block. 
- Green: block controller output voltage low, track block after signal is released, trains have permission to move in the block. 



#### Track Block Controller Design

After finished the physical world components simulation we need to develop the automate block ATC control circuit. We use PLC to implement the block control circuit so the OT engineer can easily monitor the block state and over ride the block if some emergency situation happens.

Let analysis the sensor and signal state change first, for a signal it will be changed to "on"(red) state when the block sensor is triggered then keep at on state then triggered to "off" when the next block sensor is triggered and keep off state as shown in the below table:

| Train Status                             | Sensor(n) | Sensor(n+1) | Signal-n(t) | Signal-n(t+1) |
| ---------------------------------------- | --------- | ----------- | ----------- | ------------- |
| Before train enter track block           | 0         | 0           | 0           | 0             |
| Train start enter block(passing sensor)  | 1         | 0           | 0           | 1             |
| Train entered block (passed sensor)      | 0         | 0           | 1           | 1             |
| Train leaving block(passing next sensor) | 0         | 1           | 1           | 0             |
| Train left block and in next block       | 0         | 0           | 0           | 0             |

Then if we can see the change can map to the Basic JK Flip-flop Circuit as shown below:

![](img/s_07.png)

> Reference: https://www.electronics-tutorials.ws/sequential/toggle-flip-flop.html

Now we need to find a way to generate the trigger clock. One solution is we add another senor behind the sensor(n) to create the clock, We can also use the sensor voltage change to build the clock cycle, but we can not connect both sensor(n) to J and Clk as when the clock is generated sensor(n)'s state is "unknown":

![](img/s_08.png)

To shift the clock pulse right, we need to add a delay timer. The train will take about 10 sec to pass the sensor, so we delay the sensor 1 second. Then we use an or gate to combine the 2 sensors input. The final circuit design will be shown below:

![](img/s_09.png)

**Implement the circuit via PLC ladder diagram** 

After finished design the logic in PLC. In PLC we need two contact to get the 2 sensor's voltage and one coil to change the signal state. Most of the PLC ladder editor provides the flip flop module, you can also use the NAND gate to build one if you want

![](img/s_10.png)

If you want to build your own JK flip flop ladder diagram in PLC, you can follow this document: https://instrumentationtools.com/topic/j-k-flip-flop/ The PLC ladder logic is shown below: 

![](img/s_11.png)

Wire connection: 

- sensor(n) => I0.1 => HR1
- sensor(n+1) => I0.2=>HR2
- Signal(n) => Q0.1=> C0

**Implement the circuit via PLC ST(structure text) language**

We can also use the PLC ST program language to implement the circuit. 

we create a JK flip flop function block fist: 

```pascal
FUNCTION_BLOCK JK_FlipFlop
VAR_INPUT
    J       : BOOL;   // J input
    K       : BOOL;   // K input
    CLK     : BOOL;   // Clock input
    RESET   : BOOL;   // Reset input
END_VAR

VAR_OUTPUT
    Q       : BOOL;   // Q output
    Q_NOT   : BOOL;   // Q' output (inverse of Q)
END_VAR

VAR
    last_CLK : BOOL := FALSE; // Previous state of the clock
END_VAR

// Function block implementation
IF RESET THEN
    // Asynchronous reset
    Q := FALSE;
    Q_NOT := TRUE;
ELSE
    // Detect rising edge of the clock
    IF (CLK = TRUE) AND (last_CLK = FALSE) THEN
        // Rising edge detected
        IF (J = TRUE) AND (K = FALSE) THEN
            // Set
            Q := TRUE;
            Q_NOT := FALSE;
        ELSIF (J = FALSE) AND (K = TRUE) THEN
            // Reset
            Q := FALSE;
            Q_NOT := TRUE;
        ELSIF (J = TRUE) AND (K = TRUE) THEN
            // Toggle
            Q := NOT Q;
            Q_NOT := NOT Q_NOT;
        END_IF;
    END_IF;
END_IF;

// Update last clock state
last_CLK := CLK;

END_FUNCTION_BLOCK
```



Now we make a 1 sec timer via ST language

```
FUNCTION_BLOCK TON
VAR_INPUT
    IN      : BOOL;   // Timer input
    PT      : TIME;   // Preset time
END_VAR

VAR_OUTPUT
    Q       : BOOL;   // Timer output
    ET      : TIME;   // Elapsed time
END_VAR

VAR
    start_time : TIME;   // Start time
    running    : BOOL;   // Timer running flag
END_VAR

// Function block implementation
IF IN THEN
    IF NOT running THEN
        // Start the timer
        start_time := TIME();
        running := TRUE;
    END_IF;
    // Calculate elapsed time
    ET := TIME() - start_time;
    IF ET >= PT THEN
        Q := TRUE;
    ELSE
        Q := FALSE;
    END_IF;
ELSE
    // Reset the timer
    Q := FALSE;
    ET := T#0s;
    running := FALSE;
END_IF;

END_FUNCTION_BLOCK
```

After build the 2 components module we can make our Main PLC ST program:

```
PROGRAM Main
VAR
    timer      : TON;      // Instance of the TON function block
    jkflipflop : JK_FlipFlop // Instance of the JK FLIP FLOP function block
    or_gate    : OR_Gate;  // Instance of the OR_Gate function block
    input1     : BOOL := FALSE;   // Input 1 for OR gate
    input2     : BOOL := FALSE;   // Input 2 for OR gate
    CLK_input: BOOL := FALSE;
    timer_input: BOOL := FALSE;   // Input for the timer
    preset_time: TIME := T#1s;    // Preset time for the timer (1 seconds)
    or_output  : BOOL;    // Output of the OR gate
    timer_output : BOOL;  // Output of the timer
END_VAR

// Assign inputs to the timer
timer.IN := timer_input;
timer.PT := preset_time;
// Set flip flopp in
flipflop.J := input1;
flipflop.K := input2;
// run timer
timer_input:= input1 OR input2
timer();
timer_output := timer.Q;
// Create the clock pulse
CLK_input := timer_input
flipflop.CLK := CLK_input;
// Run flipflop
flipflop();
// Get the outputs from the flip-flop
Q_output := flipflop.Q;
```



Now we can link multiple tack block control logic together to build a single track's fixed block ATC system.