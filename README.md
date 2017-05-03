#DanderSpirtz documentation
The goal of this project is to document the different capabilities and functionality of the DanderSpirtz post-exploitation framework / application by examining the contents of the "resources" folder included in the ShadowBrokers leak and doing live testing of the system.

_**Note**_: This respository does **not** contain all of the FuzzBunch code, exploits, binaries, etc. The repository _only_ contains the files found in the _Windows/Resources/_ directory included in the leak. 

If you're interested in viewing the entire contents of the leak use this repo:

[EQGRP\_Lost\_in_Translation](https://github.com/x0rz/EQGRP\_Lost\_in\_Translation)

#Python bytecode has been decompiled
The original ShadowBrokers leak had most of the python scripts compiled into optimized bytecode (.pyo). In order to make this reversing / documentation effort easier I've decompiled the code and uploaded the "raw" python code to this repository

The original python bytecode files have been left intact

#Resource Codenames and capabilities
The sub-directories in the "Resources" directory contain different modules which are used by DanderSpirtz to provide capabilities such as packet capture, memory dumps, etc. 

Below are the codenames that correspond to the differrent modules and the potentail capabilities based on examining the python code, comments, XML, available "command" txt files

**DSky** - _**Darkskyline**_ - PacketCapture tool

**DaPu** - _**DarkPulsar**_ - ???

**Darkskyline** - Contains tools to parse and filter traffic captured by DarkSkyline

**DeMI** - ??

**Df** - _**DoubleFeature**_ - ?? 

**DmGZ** - _**DoormanGauze**_ - ??

**Dsz** - _**DanderSpritz**_ - Several DanderSpritz specific files such as command descriptions (in XML), and several scripts with DSS (Debug script interface?) / DSI extensions?. They seem to be scripts run by DanderSpritz

**Ep** - _**ExpandingPulley**_ - Implant similar to PeddleCheap. DanderSpirtz can communicate with this. Should investigate further

**ExternalLibraries** - Well..

**FlAv** - _**FlewAvenue**_ - Appears related to DoormanGauze (based on FlAv/scripts/_FlewAvenue.txt)

**GRDO** - _**GreaterDoctor**_ - Appears to parse / process from GreaterSurgeon (based on GRDO/Tools/i386/GreaterSurgeon_postProcess.py & analyzeMFT.py)

**GROK** - Appears to be a keylogger (based on Ops/PyScripts/overseer/plugins/keylogger.py)

**GRcl** - Appears to dump memory from a specific process (based on GRcl/Commands/CommandLine/ProcessMemory_Command.xml)

**GaTh** - _**GangsterTheif**_ - Appears to parse data gathered by GreaterDoctor to identify other (malicious) software that may be installed persistently (based on GaTh/Commands/CommandLine/GrDo\_ProcessScanner\_Command.xml)

**GeZU** - Appears to dump memory (based on GeZu/Commands/CommandLine/GeZu\_KernelMemory\_Command.xml)

**Gui** - Resources used by the DanderSpirtz GUI

**LegacyWindowsExploits** - Well..

**Ops** - Contains a lot of awesome tools and python / dss scripts used by DanderSpritz. Deserves a lot of investigation. includes tools to gather data from Chrome, Skype, Firefox (ripper) and gather information about the machine / environment (survey)

**Pfree** - _**Passfreely**_ - Oracle implant that bypasses auth for oracle databases

**PaCU** - _**PaperCut**_ ??

**Pc** - _**PeddleCheap**_ - The main implant (loaded via DoublePulsar) that performs all of these actions and communciates with the C2 (DanderSpirtz)

**Pc2.2** - Resources for PeddleCheap including different DLLs / configs to call back to the C2

**Python** - Python Libraries / resources being used 

**ScRe** - Interacts with SQL databases (based on ScRe/Commands/CommandLine/Sql_Command.xml)

**StLa** - _**Strangeland**_ - Keylogger (based on StLa/Tools/i386-winnt/strangeland.xsl)

**Tasking** - Handles the collection "tasks" that DanderSpritz has requested on the same (collection of windows, network data, etc)

**TeDi** - _**TerritorialDispute**_ - Looks like it's a script to determine what other (malicious) software may be persistently installed (based on TeDi/PyScripts/sigs.py)

**Utbu** - _**UtilityBurst**_ - Appears to be a mechanism for persistence via a driver install _unsure_ (based on UtBu/Scripts/Include/_UtilityBurstFunctions.dsi)

**ZBng** - _**ZippyBang**_ - Looking at this quickly, it appears to be the NSA's version of Mimikatz. It can duplicate tokens (Kerberos tokens?) and "remote execute commands" as well as logon as users (based on files in ZBng/Commands/CommandLine)


**STSentrytribe (ST)
Territorialdispute (Tedi) - Seems like some kind of data collection script. Maybe it is used to find AV systems?  
UtilityBurst (UtBu) - ??
Extremelbail - Force the logon of a specific user
Zippybang (zbng) - The NSAs mimi katz
FlewAvenue (FlAV) - 
Killsuit - 
BroughtHotShot
DoubleFeature (DF) - 
GansterThief (GaTH) - 
DoormanGauze (dmGZ) - 
DanderSpritz (DSZ) 
DoorwayNapkin
ExpandingPulley - This seems huge! This is similar to peddlecheap! 
Gezu - Dumps memory
Glcl - Dumps process memory
GreaterDoctor - Master File Table parser 
GreaterSurgeon - Analysis data gathered by GreaterDoctor
Grok - ?? - Potential key logger based on data in \ops\pyscrips\overseer\plugins\keylogger.py
Ops Folder:
    Ripper - Gets chrome, Skype, firefox, etc
    Overseers - Pulls data? 
    scansweep - Like nmap?
PaperCut (PaCu) - 
ScRe - Seems to do SQL related stuff. 
