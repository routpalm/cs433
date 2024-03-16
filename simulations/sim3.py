from .simulation import *
from router import *
from secure_router import *
from simple_blockchain import Blockchain


def sim3():
    """
    Simulation 3:
    """
    AS1_config = ('localhost', 1, 5001)
    AS2_config = ('localhost', 2, 5002)
    AS3_config = ('localhost', 3, 5003)
    AS4_config = ('localhost', 4, 5004)
    AS5_config = ('localhost', 5, 5005)
    AS6_config = ('localhost', 6, 5006)
    AS7_config = ('localhost', 7, 5007)
    AS8_config = ('localhost', 8, 5008)
    AS9_config = ('localhost', 9, 5009)
    blockchain = Blockchain()
    AS1 = EBGPRouter(*AS1_config)
    AS2 = SecureEBGP(*AS2_config, blockchain)
    AS3 = EBGPRouter(*AS3_config)
    AS4 = EBGPRouter(*AS4_config)
    AS5 = EBGPRouter(*AS5_config)
    AS6 = EBGPRouter(*AS6_config)
    AS7 = EBGPRouter(*AS7_config)
    AS8 = SecureEBGP(*AS8_config, blockchain)
    AS9 = SecureEBGP(*AS9_config, blockchain)
    AS1.add_neighbors([AS2_config, AS4_config])
    AS2.add_neighbors([AS1_config, AS3_config, AS4_config, AS5_config])
    AS3.add_neighbors([AS2_config, AS5_config])
    AS4.add_neighbors([AS1_config, AS2_config, AS5_config])
    AS5.add_neighbors([AS2_config, AS3_config, AS4_config, AS7_config, AS8_config])
    AS6.add_neighbors([AS8_config, AS9_config])
    AS7.add_neighbors([AS5_config])
    AS8.add_neighbors([AS5_config, AS6_config])
    AS9.add_neighbors([AS6_config])
    for AS in [AS1, AS2, AS3, AS4, AS5, AS6, AS7, AS8, AS9]: AS.start()
    AS9.advertise_route("192.168.1.0/24")
    print(blockchain)
    print("AS 1:", AS1.routing_table["192.168.1.0/24"])
    print("AS 2:", AS2.routing_table["192.168.1.0/24"])
    print("AS 3:", AS3.routing_table["192.168.1.0/24"])
    print("AS 4:", AS4.routing_table["192.168.1.0/24"])
    print("AS 5:", AS5.routing_table["192.168.1.0/24"])
    print("AS 6:", AS6.routing_table["192.168.1.0/24"])
    print("AS 7:", AS7.routing_table["192.168.1.0/24"])
    print("AS 8:", AS8.routing_table["192.168.1.0/24"])
    print("AS 9:", AS9.routing_table["192.168.1.0/24"])
    print('Simulation ended. Press control + c to end this process.')


Simulation().add(fun=sim3, num_id=3)