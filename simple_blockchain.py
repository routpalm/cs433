'''
    test blockchain, simplest possible (?)
    referencing https://medium.com/pythoneers/building-a-blockchain-from-scratch-with-python-489e7116142e
    and https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/
'''


import hashlib
import time


'''
    a blockchain is basically like a linked list of block objects that have unique properties and are crypto-
    graphically linked. each block has a set of values and the ability to calculate it's own hash, which
    is used to make sure that the blockchain is immutable.
'''
class Block:
    # done on block creation
    def __init__(self, index, previous_hash,data : list,timestamp=None):
        '''
            self explanatory, which index in the chain it is at
        '''
        self.index = index
        '''
            chain needs to know hash of the previous block, so that if someone tries to modify the block
            the block in front of it will be able to tell.
        '''
        self.previous_hash = previous_hash 
        '''
            - determine chronological order of blocks in the chain
            - might be useful if we ever implement a Proof of Work consensus algo
            - checking validity of block
        '''
        self.timestamp = timestamp or time.time() 
        '''
            Data should be a list of the form [Origin AS, Path, Prefix, signature]
            -Origin AS (string): this is the AS that claims to have possesion of the prefix
            -Path (string): string of integers where leftmost is start of path
            -Prefix: the given IP prefix
            -Signature: the person who wrote the block's signature
        '''
        self.data = data
        '''
            stands for "number only used once", rather than the british word for pedophile. 
            added randomness and important for the mining process. more info in the source
            https://www.investopedia.com/terms/n/nonce.asp
        '''
        self.nonce = 0 
        '''
            individual hash for the block
        '''
        self.hash = self.calculate_hash()

    '''
        the hash of each block is comprised of a string based on its index, timestamp, data, and nonce.
        hashlib.sha256(prehashed.encode()) returns a binary hash that is then converted into a hexadecimal string
    '''
    def calculate_hash(self):
        prehashed = str(self.index) + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(prehashed.encode()).hexdigest()
    

class Blockchain:
    def __init__(self):
        '''
            chain here is basically an array 
        '''
        self.chain = [self.create_genesis_block()]

        '''
            This will contain each subscribed as's neighbors for verification of paths
        '''
        self.as_neighbors = {}
    

    def create_genesis_block(self):
        '''
        The genesis block is the first block in the chain. it will always have the same hash value.
        '''
        return Block(0, "0", "Genesis Block")
    
    def get_latest_block(self):
        '''
        gets most recently added block so that new blocks can get the hash of the previous block easier
        '''
        return self.chain[-1]

    def add_block(self, new_block):
        '''
        mechanism for adding new blocks
        '''
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        '''
        checks integrity of the entire chain. iterates through all blocks (except genesis) and checks:
        1. whether the hash of each block matches the hash it *should* have
        2. whether the previous hash of each block matches the hash of the previous block in the chain
        if any conditions fail, chain is invalid (tampering)
        '''
        for i in range(1,len(self.chain)):
            cur_block = self.chain[i]
            prev_block = self.chain[i-1]
            if cur_block.hash != cur_block.calculate_hash():
                return False
            if cur_block.previous_hash != prev_block.hash:
                return False
        return True
    
    def add_as_neighbors(self, as_num: str, neighbors: list):
        self.as_neighbors[as_num]=neighbors
    

'''
    testing
'''
# init chain
test_chain = Blockchain()

# add blocks
test_chain.add_block(Block(1, test_chain.get_latest_block().hash, ["1", "1", "128.0.0/24", "1"]))
test_chain.add_block(Block(2, test_chain.get_latest_block().hash, ["2", "2", "128.1.0/24", "2"]))
test_chain.add_block(Block(2, test_chain.get_latest_block().hash, ["3", "3", "128.2.0/24", "3"]))
#add neighbors
test_chain.add_as_neighbors("1", ["2"])
test_chain.add_as_neighbors("2", ["1"])
test_chain.add_as_neighbors("3", ["2"])
print(test_chain.as_neighbors)

# check validity
print("valid? (scenario 0: simple test)", test_chain.is_valid())

# print blocks
for block in test_chain.chain:
    print(f"Block {block.index} - Data: {block.data} - Hash: {block.hash}")

# tampering scenario numero uno (remember 'pointers' in python) 
# block data is modified
invalid_block = test_chain.chain[1]
invalid_block.data = "invalid"
invalid_block.hash = invalid_block.calculate_hash()

# check validity
print("valid? (scenario 1)", test_chain.is_valid())

# tampering scenario numero due
# chain is broken due to changing hash values
test_chain.chain[2].previous_hash = test_chain.chain[0].hash

# check validity
print("valid? (scenario 2)", test_chain.is_valid())