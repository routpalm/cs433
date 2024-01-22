# A Blockchain solution to BGP Route Hijacking

## Team Members: Geoff, Joseph and Nick

## Problem Statement
Problem Statement: The internet contains Autonomous Systems (AS) of ISP that can communicate with each other and advertise certain paths to websites and servers. BGP routers can however advertise a prefix that does not belong to its own AS, which illegitimately announces the prefix. This results in traffic redirection away from its destination and towards its own AS. This is known as BGP route hijacking. The real security risk is when malicious attackers announce some false prefix which leads to a fake site that can access user information and other credentials allowing the attacker to steal money, information and other credentials.

## Status Quo
One of the protocols that contributes towards the current solution to BGP route hijacking is Resource Public Key Infrastructure (RPKI). RPKI is defined as follows “Resource Public Key Infrastructure (RPKI) is a new security infrastructure to verify that an IP address block holder has authorized an Autonomous System (AS) to originate routes by maintaining a Route Origin Authorization (ROA)”[1]. The main issue is there are a few Regional Internet Registries (RIRs) that maintain cryptographic keys and certificates of the individual prefixes and IP addresses. This leads to a small set of points of failure for the security of the system. 

## Our Solution
This project is a Proof-of-Concept (PoC) that showcases a node on a (future) decentralized blockchain, henceforce called SharderChain.
