from router import EBGPRouter
from simple_blockchain import Block, Blockchain

class Secure_EBGP(EBGPRouter):
    def __init__(self, ip, as_number, port, blockchain):
        super().__init__(ip, as_number, port)
        self.blockchain = blockchain

    def write_block_to_blockchain(self, entry):
        """
        Checks to see if path can be validated by other paths in the block chain
        and adds it if so.

        Inputs:
        -path: the recieved update of a path that would like
        to be written to the blockchain
        Path will be a tuple of (Origin AS, Prefix, Path, Signature of AS writing the block)
        
        Return: True if the path was successfully writen to the blockchain
        """
        #Check if path is in blockchain
        in_chain = self.blockchain.search_for_path(entry[1])
        if in_chain == True:
            print(f"AS{entry[3]} failed to write block to chain")
            return False
        next_index = self.blockchain.get_latest_block().index + 1
        prev_hash = self.blockchain.get_latest_block().hash
        block_to_add = Block(next_index, prev_hash, entry)
        self.blockchain.add_block(block_to_add)
        print(f"AS{entry[3]} succesfuly wrote block to chain")
        return True