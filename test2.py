from secure_router import Secure_EBGP
from simple_blockchain import Blockchain, Block
from router import EBGPRouter

# init chain
test_chain = Blockchain()

#create secure routers
AS1 = Secure_EBGP("128.0.0.1", 1, 1, test_chain)
AS2 = Secure_EBGP("128.1.0.1", 2, 2, test_chain)
AS3 = Secure_EBGP("128.2.0.1", 3, 3, test_chain)
AS4 = Secure_EBGP("128.3.0.1", 4, 4, test_chain)
AS5 = Secure_EBGP("128.4.0.1", 5, 5, test_chain)
AS6 = Secure_EBGP("128.5.0.1", 6, 6, test_chain)

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
as1_n = [2,3]
as2_n = [1,4]
as3_n = [1,5]
as4_n = [2,6]
as5_n = [3,6]
as6_n = [4,5]

AS1.add_as_neighbors(as1_n)
AS2.add_as_neighbors(as2_n)
AS3.add_as_neighbors(as3_n)
AS4.add_as_neighbors(as4_n)
AS5.add_as_neighbors(as5_n)
AS6.add_as_neighbors(as6_n)

for block in test_chain.chain:
    print(block.data)

#verify path from AS1
result = AS1.verify_path([1,2,4,6])
print(result)

#!!!!Test 2!!!!
print("-------------Test2-------------:")

#consider as2, as3, as6 are not secure routers but as1, as4, and as5 are. 
test2_chain = Blockchain()

#create secure routers
AS1 = Secure_EBGP("128.0.0.1", 1, 1, test2_chain)
AS2 = EBGPRouter("128.1.0.1", 2, 2)
AS3 = EBGPRouter("128.2.0.1", 3, 3)
AS4 = Secure_EBGP("128.3.0.1", 4, 4, test2_chain)
AS5 = Secure_EBGP("128.4.0.1", 5, 5, test2_chain)
AS6 = EBGPRouter("128.5.0.1", 6, 6,)

as1_n = [2,3]
as4_n = [2,6]
as5_n = [3,6]

AS1.add_as_neighbors(as1_n)
AS4.add_as_neighbors(as4_n)
AS5.add_as_neighbors(as5_n)

for block in test2_chain.chain:
    print(block.data)
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
AS1 = Secure_EBGP("128.0.0.1", 1, 1, test3_chain)
AS2 = EBGPRouter("128.1.0.1", 2, 2)
AS3 = EBGPRouter("128.2.0.1", 3, 3)
AS4 = Secure_EBGP("128.3.0.1", 4, 4, test3_chain)
AS5 = EBGPRouter("128.4.0.1", 5, 5)
AS6 = EBGPRouter("128.5.0.1", 6, 6,)

as1_n = [2,3]
as4_n = [2,6]

AS1.add_as_neighbors(as1_n)
AS4.add_as_neighbors(as4_n)
for block in test3_chain.chain:
    print(block.data)

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
