# Forensic-Scenario-Builder

The goal is to automatically stand up a private network that spawns predefined containers/vms and runs through a defined scenario. Once the scenario is finished the builder will create and return the requested forensic artifacts. An example scenario built could be defining a victim web server, a bunch of traffic creation bots that make requests to the web server, and an attacker that hacks into the web server. After the attack is done the web server logs are pulled off of the victim vm and a pcap of the traffic from the scenario is created.

## Design
### Goals
- Automatic container/vm creation with docker(?) and vagrant(?)
- Automatic network creation 
- Automatic traffic creation
- Automatic attack
- Automatic artifact creation
  - Logs
  - Disk Image
  - Memory Image
  - Pcaps
  - Etc
- Automatic teardown

### CLI Interface
- bot
  - Location of file describing bot container or vm
- bot-num
  - Number of bot containers to spawn
  - Default to one or two
- attacker
  - Location of file describing attacker container or vm
- attacker-ip
  - Assign static ip to attacker
  - Default to random
- victim
  - Location of file describing victim container or vm
- victim-ip 
  - Assign static ip to victim
  - Default to random
- logs
  - Location to pull log file(s) from on victim after scenario is done
- disk-image
  - Create disk image of victim after scenario is done
- memory-dump
  - Create memory dump of victim after scenario is done
- pcap 
  - Create pcap of scenario traffic
- subnet 
  - Subnet to place scenarios and containers on
  - Default to 10.0.0.0/8


