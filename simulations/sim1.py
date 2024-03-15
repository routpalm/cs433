from .simulation import *
from router import *
import sys

def sim1():
    """
    Simulation 1:
        Three regular routers talk to each other.
    """
    router1 = EBGPRouter('localhost', 1, 5001)
    router2 = EBGPRouter('localhost', 2, 5002)
    router3 = EBGPRouter('localhost', 3, 5003)
    router4 = EBGPRouter('localhost', 4, 5004)
    router5 = EBGPRouter('localhost', 5, 5005)
    router6 = EBGPRouter('localhost', 6, 5006)
    router7 = EBGPRouter('localhost', 7, 5007)
    router8 = EBGPRouter('localhost', 8, 5008)
    router9 = EBGPRouter('localhost', 9, 5009)
    router1.add_neighbor('localhost', 2, 5002)  # r1 -> r2
    router1.add_neighbor('localhost', 4, 5004)  # r1 -> r4
    router2.add_neighbor('localhost', 1, 5001)  # r2 -> r1
    router2.add_neighbor('localhost', 5, 5005)  # r2 -> r3
    router2.add_neighbor('localhost', 4, 5004)  # r2 -> r4
    router2.add_neighbor('localhost', 3, 5003)  # r2 -> r5
    router3.add_neighbor('localhost', 2, 5002)  # r3 -> r2
    router3.add_neighbor('localhost', 5, 5005)  # r3 -> r5
    router4.add_neighbor('localhost', 1, 5001)  # r4 -> r1
    router4.add_neighbor('localhost', 2, 5002)  # r4 -> r2
    router4.add_neighbor('localhost', 5, 5005)  # r4 -> r5
    router5.add_neighbor('localhost', 2, 5002)  # r5 -> r2
    router5.add_neighbor('localhost', 3, 5003)  # r5 -> r3
    router5.add_neighbor('localhost', 4, 5004)  # r5 -> r4
    router5.add_neighbor('localhost', 6, 5006)  # r5 -> r6
    router5.add_neighbor('localhost', 7, 5007)  # r5 -> r7
    router5.add_neighbor('localhost', 8, 5008)  # r5 -> r8
    router6.add_neighbor('localhost', 5, 5005)  # r6 -> r5
    router6.add_neighbor('localhost', 8, 5008)  # r6 -> r8
    router6.add_neighbor('localhost', 9, 5009)  # r6 -> r9
    router7.add_neighbor('localhost', 5, 5005)  # r7 -> r5
    router8.add_neighbor('localhost', 5, 5005)  # r8 -> r5
    router8.add_neighbor('localhost', 6, 5006)  # r8 -> r6
    router9.add_neighbor('localhost', 6, 5006)  # r9 -> r6
    router1.start()
    router2.start()
    router3.start()
    router4.start()
    router5.start()
    router6.start()
    router7.start()
    router8.start()
    router9.start()
    router9.advertise_route("192.168.1.0/24")
    print(1, router1.routing_table["192.168.1.0/24"])
    print(2, router2.routing_table["192.168.1.0/24"])
    print(3, router3.routing_table["192.168.1.0/24"])
    print(4, router4.routing_table["192.168.1.0/24"])
    print(5, router5.routing_table["192.168.1.0/24"])
    print(6, router6.routing_table["192.168.1.0/24"])
    print(7, router7.routing_table["192.168.1.0/24"])
    print(8, router8.routing_table["192.168.1.0/24"])
    print(9, router9.routing_table["192.168.1.0/24"])
    print('Simulation ended. Press control + c to end this process.')

Simulation().add(fun=sim1, num_id=1)