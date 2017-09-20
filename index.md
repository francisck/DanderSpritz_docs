---
layout: default
---

# [](#header-1)DanderSpirtz documentation

The goal of this project is to document the different capabilities and functionality of the DanderSpirtz post-exploitation framework by examining the contents of the “resources” folder included in the ShadowBrokers leak _and_ doing live testing of the framework on lab systems. 

_Note_: This is a documentation project that does **not** contain all of the FuzzBunch code, exploits, binaries, etc. The repository only contains the files found in the Windows/Resources/ directory included in the leak.

If you’re interested in viewing the entire contents of the leak use this repo _including_ the files and data necessary to use the framework, please use this repo:

[EQGRP Lost in Translation](https://github.com/x0rz/EQGRP/_Lost/_in/_Translation).

_**Disclaimer**_: This project is intended to be used by information security researchers who are interested in understanding the capabilities of frameworks used by real-life nation state adversaries. I am not responsible if you choose to use my work or this documentation to do something dumb and illegal. 

## [](#header-2)What is DanderSpritz? 

DanderSpritz is a modular, stealthy, and fully functional framework for post-exploitation activities on Windows and Linux hosts. The framework contains tools to bypass anti-virus & security tools, disable and delete Windows event logs, establish persistence, perform local and network reconnaissance, move laterally within a network, and exfiltrate data. 

DanderSpritz was leaked by [The Shadow Brokers](https://en.wikipedia.org/wiki/The_Shadow_Brokers) on April 14th, 2017 as part of the "[Lost in Translation](https://www.bleepingcomputer.com/news/security/shadow-brokers-release-new-files-revealing-windows-exploits-swift-attacks/)" leak. 

![](https://cdn-images-1.medium.com/max/1000/0*ano1zqapZ9m4QWyb.png)

## [](#header-2)Framework Documentation

*   [Setting up DanderSpritz](setup)
*   [DanderSpritz Terms & Code Names](terms)
*   [DanderSpritz Operations](operation)
*   [Safety Handlers](safety)
*   [AV & Security Product Bypasses](psp_bypass)
*   [Logging Bypasses & Modifications](logging_bypass)
*   [Local Reconnaissance](local_recon)
*   [Network Reconnaissance](network_recon)
*   [Persistence Methods](persistence)
*   [Lateral Movement](lateral)
*   [Data Identification and Exfiltration](exfil)

## [](#header-2)Blog Posts

*   [DanderSpritz Overview Part 1 (Information gathering, AV bypasses, and security auditing bypasses)](https://medium.com/francisck/the-equation-groups-post-exploitation-tools-danderspritz-and-more-part-1-a1a6372435cd)
*   This is an unordered list following a header.
*   This is an unordered list following a header.

## [](#header-2)Presentation 

A recording of my presentation about DanderSpritz at Derbycon 7.0 is coming soon


