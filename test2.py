from secure_router import SecureEBGP
from simple_blockchain import Blockchain, Block
from router import EBGPRouter

# init chain
test_chain = Blockchain()

#create secure routers
AS1_config = ("localhost", 1, 5001)
AS2_config = ("localhost", 2, 5002)
AS3_config = ("localhost", 3, 5003)
AS4_config = ("localhost", 4, 5004)
AS5_config = ("localhost", 5, 5005)
AS6_config = ("localhost", 6, 5006)
AS1 = SecureEBGP(*AS1_config, test_chain)
AS2 = SecureEBGP(*AS2_config, test_chain)
AS3 = SecureEBGP(*AS3_config, test_chain)
AS4 = SecureEBGP(*AS4_config, test_chain)
AS5 = SecureEBGP(*AS5_config, test_chain)
AS6 = SecureEBGP(*AS6_config, test_chain)
'''
Topology
    AS2 - AS4
    /       \
AS1          AS6
    \       /
    AS3- AS5

'''
#!!!!Test 1!!!!
print("-------------Test1-------------:")
# add neighbors
AS1.add_neighbors([AS2_config, AS3_config])
AS2.add_neighbors([AS1_config, AS4_config])
AS3.add_neighbors([AS1_config, AS5_config])
AS4.add_neighbors([AS2_config, AS6_config])
AS5.add_neighbors([AS3_config, AS6_config])
AS6.add_neighbors([AS4_config, AS5_config])
print(test_chain)

#verify path from AS1
result = AS1.verify_path([1,2,4,6])
print(result)

#!!!!Test 2!!!!
print("-------------Test2-------------:")

#consider as2, as3, as6 are not secure routers but as1, as4, and as5 are. 
test2_chain = Blockchain()

#create secure routers
AS1_config = ("localhost", 1, 5001)
AS2_config = ("localhost", 2, 5002)
AS3_config = ("localhost", 3, 5003)
AS4_config = ("localhost", 4, 5004)
AS5_config = ("localhost", 5, 5005)
AS6_config = ("localhost", 6, 5006)
AS1 = SecureEBGP(*AS1_config, test2_chain)
AS2 = EBGPRouter(*AS2_config)
AS3 = EBGPRouter(*AS3_config)
AS4 = SecureEBGP(*AS4_config, test2_chain)
AS5 = SecureEBGP(*AS5_config, test2_chain)
AS6 = EBGPRouter(*AS6_config)
AS1.add_neighbors([AS2_config, AS3_config])
AS2.add_neighbors([AS1_config, AS4_config])
AS3.add_neighbors([AS1_config, AS5_config])
AS4.add_neighbors([AS2_config, AS6_config])
AS5.add_neighbors([AS3_config, AS6_config])
AS6.add_neighbors([AS4_config, AS5_config])
print(test2_chain)

#Secure Paths:
result2 = AS1.verify_path([1,2,4,6])
print(f"Path: 1, 2, 4, 6 is {result2}")
result3 = AS1.verify_path([1,3,5,6])
print(f"Path: 1, 3, 5, 6 is {result3}")
result4 = AS1.verify_path([1, 3, 5, 6, 4, 2, 1])
print(f"Path: 1, 3, 5, 6, 4, 2, 1 is {result4}")

#Non Secure Paths:
result6 = AS1.verify_path([1,3,4,6])
print(f"Path: 1, 3, 4, 6 is {result6}")
result7 = AS1.verify_path([1,3,5,6,2])
print(f"Path: 1, 3, 5, 6, 2 is {result7}")

#!!!!Test 3!!!!
print("-------------Test3-------------:")
test3_chain = Blockchain()

#create secure routers
AS1_config = ("localhost", 1, 5001)
AS2_config = ("localhost", 2, 5002)
AS3_config = ("localhost", 3, 5003)
AS4_config = ("localhost", 4, 5004)
AS5_config = ("localhost", 5, 5005)
AS6_config = ("localhost", 6, 5006)
AS1 = SecureEBGP(*AS1_config, test3_chain)
AS2 = EBGPRouter(*AS2_config)
AS3 = EBGPRouter(*AS3_config)
AS4 = SecureEBGP(*AS4_config, test3_chain)
AS5 = EBGPRouter(*AS5_config)
AS6 = EBGPRouter(*AS6_config)
AS1.add_neighbors([AS2_config, AS3_config])
AS4.add_neighbors([AS2_config, AS6_config])
print(test3_chain)

#Secure Paths
result8 = AS1.verify_path([1,2,4,6])
print(f"Path: 1, 2, 4, 6 is {result8}")
result9 = AS1.verify_path([6, 4, 2, 1])
print(f"Path: 6, 4, 2, 1 is {result9}")

#Non Secure Paths:
result10 = AS1.verify_path([1, 3, 5, 6])
print(f"Path: 1, 3, 5, 6 is {result10}")
result11 = AS1.verify_path([6, 5, 3, 1])
print(f"Path: 1, 3, 5, 6 is {result10}")
