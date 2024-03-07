from router import EBGPRouter
from simple_blockchain import Blockchain
import time

#Initialize Blockchain
blockchain = Blockchain()

router1 = EBGPRouter("127.0.0.1", 100, 12000)
router2 = EBGPRouter("127.0.0.1", 200, 12001)

#add neighbors
router1.add_neighbor("127.0.0.1", 12001)
router2.add_neighbor("127.0.0.1", 12000)

router1.start()
router2.start()

# advertise a route from each router
router1.advertise_route("10.0.0.0/24")
time.sleep(2)
router2.advertise_route("20.0.0.0/24")
time.sleep(2)