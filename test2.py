from secure_router import Secure_EBGP
from simple_blockchain import Blockchain, Block

# init chain
test_chain = Blockchain()

#create secure routers
AS1 = Secure_EBGP("128.0.0.1", "1", 1, test_chain)
AS2 = Secure_EBGP("128.1.0.1", "2", 2, test_chain)
AS3 = Secure_EBGP("128.2.0.1", "3", 3, test_chain)

# add blocks
test_chain.add_block(Block(1, test_chain.get_latest_block().hash, ["1", "1", "128.0.0/24", "1"]))
test_chain.add_block(Block(2, test_chain.get_latest_block().hash, ["2", "2", "128.1.0/24", "2"]))
test_chain.add_block(Block(3, test_chain.get_latest_block().hash, ["3", "3", "128.2.0/24", "3"]))

#add neighbors
test_chain.add_as_neighbors("1", ["2"])
test_chain.add_as_neighbors("2", ["1"])
test_chain.add_as_neighbors("3", ["2"])
print(test_chain.as_neighbors)

#Update Scenario 1: as1 recieves update from as2 saying get to prefix 128.1.0/24 through me that is path 12
entry = ["2", "21", "128.1.0/24","1"]
verified = AS1.verify_path(entry)
if verified:
    print("Path was verified, writing to chain")
    AS1.write_block_to_blockchain(entry)
else:
    print("Path was not verified")

#Update Scenario 2: as1 recieves update that is in blockchain
entry = ["2", "21", "128.1.0/24","2"]
verified = AS2.verify_path(entry)
if verified:
    print("Path was verified")
    AS2.write_block_to_blockchain(entry)
else:
    print("Path was not verified")

#Update Scenario 3: as3 recieves update that it can get to 1 through 2
entry = ["1", "123", "128.0.0/24","3"]
verified = AS3.verify_path(entry)
if verified:
    print("Path was verified")
    AS3.write_block_to_blockchain(entry)
else:
    print("Path was not verified")

for block in test_chain.chain:
    print(block.data)