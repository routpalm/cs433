# A Blockchain solution to BGP Route Hijacking

## Team Members: Geoff, Joseph and Nick

## Problem Statement
Problem Statement: The internet contains Autonomous Systems (AS) of ISP that can communicate with each other and advertise certain paths to websites and servers. BGP routers can however advertise a prefix that does not belong to its own AS, which illegitimately announces the prefix. This results in traffic redirection away from its destination and towards its own AS. This is known as BGP route hijacking. The real security risk is when malicious attackers announce some false prefix which leads to a fake site that can access user information and other credentials allowing the attacker to steal money, information and other credentials.

## Status Quo
The current problem with BGP is the myopia of each router. Routers cannot see context outside of the limited amount of information they are given, so thusly each BGP router has a "fog of war" around itself that is permeated only by the often infrequent route announcements or withdrawals.

## Our Solution
This project is a Proof-of-Concept (PoC) that showcases a node on a blockchain, henceforce called SharderChain. Our goal is to use the blockchain as a ledger to allow routers to reconstruct route propogation history and make decisions based on how secure of a path it followed. By keeping the propogation history of every prefix and every path, BGP routers have a much wider view of the BGP topography and are able to make more informed routing decisions as a result. 
