---
layout: content
---

[Home](./)

# [](#header-1)DanderSpirtz Operations


Operations allow DanderSpritz to centrally collect all data related to an attack against a particular organization. 

- All session data (commands, logs, screenshots, exfiltrated data, etc) collected by DanderSpritz across all targets are stored in the operation's directory. 
- By default, DanderSpritz wants to create a new private / public key pair for C&C communication for each unique operation.
- DanderSpritz has the capability to correlate data across targets within the same operation and show the operator if the following items were seen previously on other targets:
- Unknown or suspicious drivers drivers
- Personal Protection Products (PSP)
- Unknown or suspicious services
- Unknown or suspicious registry keys 
- Potential methods of persistence 
- [Safety Handlers](safety) can be registered across an entire operation
- DanderSpritz has the capability to replay operations by using the ```ReplayingWizard.py``` script included in the "```D:\DSZOPSDISK```" folder
- Operational Notes (```opsnotes.txt```) can be parsed to automatically create "Technical Summaries" that can be shared about an operation


## [](#header-2)Operation Folder

Operations can easily be created using the FuzzBunch tool's wizard and are automatically created in:

```D:\logs\$OPERATION_NAME```

## [](#header-2)Contents of an operation's folder

__This content is still under construction__

DanderSpirtz and Fuzzbunch will each create a separate folder for each individual target: By default, DanderSpritz names targets in the following format:

```z0.0.0.[_digit_]```

The last digit will automatically increment as DanderSpritz connects to more targets. 

|      Folder / File                   |       Contents        |
|:         ---                         |:------------------------|
|**GuiRequestLog**                     | |
|**GuiSystemLog**                      | |
|**Logs**                              | |
|**Targetdbs**                         | |
|**$TARGET_FOLDER**                    | |
|**config.xml**                        | |

## [](#header-2)Contents of a Specific Target's folder

|      Folder / File                   |       Contents        |
|:         ---                         |:------------------------|
|**Data**                              | |
|**GetFiles**                          |Data exfiltrated and downloaded from the target|
|**LegacyExploits**                    |Legacy exploits launched _from_ the target against another machine |
|**Logs**                              |Logs from all commands run on the target in XML format with results & data returned|
|**Payloads**                          |Payloads generated and configured on the target by DanderSpritz (likely peddlecheap) and used to move laterally |
|**Screenshots**                       |Screenshots taken on the target (either manually using the ```screenshot``` command or automatically by another tool|
|**Tasking**                           | |
|**tmp**                               | |
|**UsedTools**                         | |
|**connect_$DATETIME.xml**             | |
|**donuts.json**                       | |
|**host_$DATETIME.txt**                | |
|**host_$DATETIME.xml**                | |