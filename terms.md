---
layout: content
---

[Home](./)

# [](#header-1)DanderSpritz Terms & Code Names

The goal of this project is to document the different capabilities and functionality of the DanderSpirtz post-exploitation framework by examining the contents of the “resources” folder included in the ShadowBrokers leak _and_ doing live testing of the framework on lab systems. 

_Note_: This is a documentation project that does **not** contain all of the FuzzBunch code, exploits, binaries, etc. The repository only contains the files found in the Windows/Resources/ directory included in the leak.

If you’re interested in viewing the entire contents of the leak use this repo _including_ the files and data necessary to use the framework, please use this repo:

[EQGRP Lost in Translation](https://github.com/x0rz/EQGRP/_Lost/_in/_Translation).

## [](#header-2)Terms

|      Term                            |       Description        |
|:         ---                         |:------------------------:|
|**Target**                            |The machine to which DanderSpritz is connected |
|**Operation**                         |A collection of target data. Targets from the same organization should be grouped into the same _operation_|
|**Listening Post** (LP)               |The command & control (C&C) server to which the target calls back or accepts connections from. The machine that is running DanderSpritz is the "LP"|
|**Plugin**                            |Some functionality provided by either a command, a python script, or a "DSS" script|
|**Command**                           |A task issued to the target via DanderSpritz|
|**Personal Protection Product** (PSP) |Anti-virus or a security product running on the target machine|
|**Safety Handler**                    |Designed to prevent certain actions or commands in order to avoid detection by PSPs, logging, or by the user|


## [](#header-2)Code Names

|       Shortname          |       Code Name          | Description        |
|:         ---            :|:         ---            :|:       ---        :|
|**DSky**                  | _**Darkskyline**_        | PacketCapture tool | 
|**DaPu**                  | _**DarkPulsar**_         | Appears to be a legacy implant, similar to PeddleCheap but older |
|**DeMI**                  | _**DecibelMinute**_      | Appears to interact with KillSuit to install, configure, and uninstall it |
|**Df**                    | _**DoubleFeature**_      | Generates a log & report about the types of tools that could be deployed on the target. A lot of tools mention that _doublefeature_ is the only way to confirm their existence|
|**DmGZ**                  | _**DoormanGauze**_       | DoormanGauze is a kernel level network driver that appears to bypass the standard Windows TCP/IP stack|
|**Dsz**                   | _**DanderSpritz**_       | Several DanderSpritz specific files such as command descriptions (in XML), and several scripts with DSS (Debug script interface?) / DSI extensions?. They seem to be scripts run by DanderSpritz |
|**Ep**                    | _**ExpandingPulley**_    |Listening Post developed in 2001 and abandoned in 2008. Predecessor to DanderSpritz|
|**FlAv**                  | _**FlewAvenue**_         | Appears related to DoormanGauze (based on FlAv/scripts/_FlewAvenue.txt) |
|**GRDO**                  | _**GreaterDoctor**_      | Appears to parse / process from GreaterSurgeon (based on GRDO/Tools/i386/GreaterSurgeon_postProcess.py & analyzeMFT.py) |
|**GROK**                  |           ??             | Appears to be a keylogger (based on Ops/PyScripts/overseer/plugins/keylogger.py) |
|**GRcl**                  |           ??             | Appears to dump memory from a specific process (based on GRcl/Commands/CommandLine/ProcessMemory_Command.xml) |
| **GaTh**                 | _**GangsterTheif**_      | Appears to parse data gathered by GreaterDoctor to identify other (malicious) software that may be installed persistently (based on GaTh/Commands/CommandLine/GrDo\_ProcessScanner\_Command.xml) |
| **GeZU**                 | _**GreaterSurgeon**_      | Appears to dump memory (based on GeZu/Commands/CommandLine/GeZu\_KernelMemory\_Command.xml) |
|**Pfree**                 | _**Passfreely**_         | Oracle implant that bypasses auth for oracle databases |
|**PaCU**                  | _**PaperCut**_           | Allows you to perform operations on file handles opened by other processes |
|**Pc**                    | _**PeddleCheap**_        | The main implant (loaded via DoublePulsar or another backdoor) that communicates with the C2 (DanderSpirtz) and performs actions |
|**ScRe**                  |          ??              | Interacts with SQL databases (based on ScRe/Commands/CommandLine/Sql_Command.xml) |
|**StLa**                  | _**Strangeland**_        | Keylogger (based on StLa/Tools/i386-winnt/strangeland.xsl) |
|**TeDi**                  | _**TerritorialDispute**_ | - Looks like it's a script to determine what other (malicious) software may be persistently installed (based on TeDi/PyScripts/sigs.py)
|**Utbu**                  | _**UtilityBurst**_       | Appears to be a mechanism for persistence via a driver install _unsure_ (based on UtBu/Scripts/Include/_UtilityBurstFunctions.dsi) |
|**ZBng**                  | _**ZippyBang**_          | Looking at this quickly, it appears to be the NSA's version of Mimikatz. It can duplicate tokens (Kerberos tokens?) and "remote execute commands" as well as logon as users (based on files in ZBng/Commands/CommandLine) |
