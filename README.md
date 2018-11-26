# firewall_rules
get windows firewall rules

There are two scripts powershell and python that should copy be copied to win machine. First you should run the powershell script, that create file rules.txt in current dir. This file collect all windows firewall rules on current PC. Python script based on rules.txt and prints out information about requested rules. (python 3 required).
Here is an example of the conclusion of 5 rules:

5 rules to select

Firewall rules:
        Remote Event Log Management (RPC-EPMAP) - Local
        File and Printer Sharing (NB-Name-Out) - Local
        Play To streaming server (HTTP-Streaming-In) - Local
        Media Center Extenders - HTTP Streaming (TCP-In) - Local
        Connect to a Network Projector (WSD EventsSecure-Out) - Local
        
Inbound: 3
Outbound: 2

Enabled: 1
Disabled: 4
