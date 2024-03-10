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
        next_index = self.blockchain.get_latest_block().index + 1
        prev_hash = self.blockchain.get_latest_block().hash
        block_to_add = Block(next_index, prev_hash, entry)
        self.blockchain.add_block(block_to_add)
        print(f"AS{entry[3]} succesfuly wrote block to chain")
        return True
    
    def search_for_path(self, path):
        for Block in self.blockchain.chain:
            if Block.data[1] == path:
                return True
            
        return False

    def verify_path(self, entry):
        """
        This method will take an entry (of the form Block.data) and attempt to form
        and verify the entries path from the blockchain.
        """
        #Verify the path can be produced from existing paths in blockchain
        path_build = [0 for i in range(len(entry[1])-1)]
        for asx in range(len(entry[1])-1):
            #This is the as that sent the path update so we check neighbors of as 
            if asx+1 == len(entry[1])-1:
                valid_neighbor = False
                for neighbor in self.blockchain.as_neighbors[entry[1][asx+1]]:
                    if neighbor == entry[1][asx]:
                        #the neighbor is a valid neighbor
                        path_build[asx] = 1
                        valid_neighbor = True
                        break
                if valid_neighbor:
                    break
                else:
                    print("Not a neighbor")
                    return False  
            asy = asx + 1
            for block in self.blockchain.chain:
                confirmed = False
                for asz in range(len(block.data[1])-1):
                    if block.data[1][asz] == entry[1][asx] and block.data[1][asz+1] == entry[1][asy]:
                        path_build[asx] = 1
                        confirmed = True
                        break
                    if block.data[1][asz] == entry[1][asy] and block.data[1][asz+1] == entry[1][asx]:
                        path_build[asx] = 1
                        confirmed = True
                        break
                #If it was verified that the path from asx to asy exists in blockchain break
                if confirmed:
                    break
        verified = True
        for i in range(len(entry[1])-1):
            if path_build[i] == 0:
                verified = False
                break

        if not verified:
            print(f"AS{entry[3]} failed to add {entry[1]}: path could not be validated {path_build}")
            return False
        else:
            return True