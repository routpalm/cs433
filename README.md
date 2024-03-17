# A Blockchain solution to BGP Myopia

## Team Members: Geoff, Joseph and Nick

## Abstract
A growing constriction in the world of BGP security is the nearsightedness of BGP routers. Simply put, BGP routers cannot reconstruct route propagation history, so their knowledge of their own surrounding topography is limited at best. Additionally, with the most common BGP security protocol, BGPSec, security features are dropped if a secure BGP packet passes through a router that does not implement the protocol. This requires that all routers in a path must implement the protocol for the path to be secure. To remedy this security issue using blockchain, multiple solutions have been suggested, but previous research in this subject has introduced methods that modify base BGP communications and administrative bodies in such a way that successful implementation would require exceeding the adoption rate of BGPSec and other security protocols. In this paper, our approach to a blockchain solution to BGP security is thus: we choose not to focus on the decentralization aspect of blockchain, but rather its ability to be an immutable ledger. By storing paths both heard and sent, routers aiming to evaluate the security of a given BGP announcement may check the blockchain and verify that the announcement traveled a secure path before arriving at the destination. Additionally, through a method we call “neighborhoods”, security may also be achieved by verifying neighbors and storing their positions in the blockchain, preventing path and origin spoofing. Our results show – preliminarily and with some restrictions –  the general algorithm behind our implementation is sound, and we can ensure that some paths can be one hundred percent secure without all routers in said path subscribing to our protocol. 


# Code Manual
There are six simulations, each with a corresponding diagram outlining network topography shown below.

To run our code, you must do the following:

## Windows
`python main.py {simulation #}`
## Mac
`python3 main.py {simulation #}`
## Example: 
`python main.py 1` - runs simulation 1

The output prints first the output of the blockchain after all announcements have been propagated. Then, it prints the routing tables of each router in the topology.

Note: Simulation 6 is a special case/for fun simulation (that is just for fun, not to be graded) that outputs a file called `sim6_blockchain.log`. It is a simulation on a large scale that may take time to run and produces thread errors/socket errors on some machines. 
However, it is readable (albeit a couple thousand lines) but it does indeed emulate the correct behavior. There is only one announcement that originates from NA AS 10 advertising the route 1.1.0.0. 
It can be found in the code at line `347`.
## Simulation Diagrams
![Simulation 1 Diagram](/simulations/sim1.png)
![Simulation 2 Diagram](/simulations/sim2.png)
![Simulation 3 Diagram](/simulations/sim3.png)
![Simulation 4 Diagram](/simulations/sim4.png)
![Simulation 5 Diagram](/simulations/sim5.png)
![Simulation 6 Diagram](/simulations/sim6.png)
