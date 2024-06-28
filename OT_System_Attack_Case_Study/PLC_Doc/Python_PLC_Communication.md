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

#### STEP2: Config the Ladder Logic 

M221 supports normal Modbus TCP protocol communication, but if you don't use the soMachine SDK, your program can not read the contact "I0.X" or write the coil "Q0.X" directly. The solution is to link the contact "I0.X" or coil "Q0.X" to a PLC memory address, then read or write the memory address to get the contact input or set the coil output. The ladder logic can be draft as shown below:

```
[ I0.x ] --> | M1.x | 
| M1.x | --> | Your Ladder Logic | --> | M2.x |
| M2.x | --> ( Q0.x )
```

Open the SoMachine ladder config page and added the ladder logic as shown below:

![](img/ladderCfg.png)

Then in the commissioning page select the "PC to Controller" to commit the Ladder logic in to the PLC as shown below:

![](img/commit.png)



#### STEP3: Understand of Communication Protocol

The M221 communicate protocol is shown below, we need to use two Modbus function code: 

- `'0f'` : Memory access function code (write) multiple bit
- `'01'` : Memory state fetch internal multiple bits %M

To use more function, please refer to the function code table in page 197 of the [M221 Manual](https://media.distributordatasolutions.com/schneider2/2020q4/documents/fbb188fbd042afd838384db125b9dad1c2a6a9e9.pdf) 

![](img/functionCode.png)

The Modbus data sequence table is shown below:

 ![](img/modbusTable.png)

Modbus message sequence to read bit data from the memory 

| TID     | PROTOCOL_ID | Length  | UID    | Function Code | Memory Idx | Bit Length |
| ------- | ----------- | ------- | ------ | ------------- | ---------- | ---------- |
| 2 bytes | 2 bytes     | 2 bytes | 1 byte | 1 byte        | 2bytes     | 2bytes     |
| `0000`  | `0000`      | `0006`  | `01`   | `01`          | `<0032>`   | `<0008>`   |

Modbus message sequence to write byte data to the memory 

| TID     | PROTOCOL_ID | Length  | UID    | Function Code | Memory Idx | Bit Index | Byte Index | Value Byte |
| ------- | ----------- | ------- | ------ | ------------- | ---------- | --------- | ---------- | ---------- |
| 2 bytes | 2 bytes     | 2 bytes | 1 byte | 1 byte        | 2bytes     | 1 byte    | 2bytes     | 1 byte     |
| `0000`  | `0000`      | `0008`  | `01`   | `0f`          | `<0032>`   | `<01>`    | `<0001>`   | `<01>`     |

For the memory tag `%MXX` to memory address, just convert the digital number to hex number (use lower case if to string) as shown example below:

```
MEM_ADDR_TAG_Example = {
    'M0':   '0000',
    'M1':   '0001',
    'M2':   '0002',
    'M3':   '0003',
    'M4':   '0004',
    'M5':   '0005',
    'M6':   '0006',
    'M10':  '000a',
    'M20':  '0014',
    'M30':  '001e',
    'M40':  '0028',
    'M50':  '0032',
    'M60':  '003c'
}
```



#### STEP 4: Use Python to Communicate with the PLC

**4.1 Init connection**

To communicate with the PLC, we need to fist init a TCP client which connect to the PLC's  IPaddress with port 502 as shown below: 

```
self.plcAgent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	self.plcAgent.connect((self.ip, self.port))
	if self.debug: print("M221Client: Connected to the PLC [%s]" % self.ip)
	self.connected = True
except Exception as error:
	print("M221Client: Can not access to the PLC [%s]" % str(self.plcAgent))
	print(error)
```

**4.2 Send message to PLC**

To send the message to PLC we need to convert the hex string to bytes type 

```
bdata = bytes.fromhex(modbusMsg)
try:
    self.plcAgent.send(bdata)
    respBytes = self.plcAgent.recv(BUFF_SZ)
    respStr = respBytes.dencode('hex') if DECODE_MD else respBytes.hex()
    self.connected = True
```

**4.3 Read the PLC memory data** 

Based on step2, build the memory read Modbus message and call the send function to read the memory bytes data from the PLC.

```
#-----------------------------------------------------------------------------
    def readMem(self, memAddrTag, bitNum=8):
        """ Fetch the current plc memory state with a bit lengh. 
            Args:
                memAddrTag (str): M221 memory tag such as "M60"
                bitNum (int, optional): number of bit to read from the memory address. Defaults to 8.
            Returns:
                _type_: hex byte string of the memory address state. example 0x0101
        """
        if str(memAddrTag).startswith('M'):
            memoryDecimal = int(memAddrTag[1:])
            memoryHex = hex(memoryDecimal)[2:]
            bitNumHex = hex(bitNum)[2:]
            modbusMsg = ''.join((TID, PROTOCOL_ID, R_LENGTH, UID, M_RD, memoryHex, bitNumHex))
            response = self._getPlCRespStr(modbusMsg)
            return response
        else:
            print("Error > readMem(): Invalid memory address [%s]" % memAddrTag)
            return None
```

**4.4 Write the PLC memory data **  

Same as the data read, build the 