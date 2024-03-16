from router import EBGPRouter
from simple_blockchain import Block, Blockchain
import json


class SecureEBGP(EBGPRouter):
    def __init__(self, ip, as_number, port, blockchain):
        super().__init__(ip, as_number, port)
        self.blockchain = blockchain

    def write_block_to_blockchain(self, data):
        """
        Creates a block and adds the data to the block. 
        Then writes the block to blockchain.

        Inputs:
        -data: May be two forms defined in simple_blockchain.py data for a block 
        Return: True if the path was successfully writen to the blockchain
        """
        next_index = self.blockchain.get_latest_block().index + 1
        prev_hash = self.blockchain.get_latest_block().hash
        block_to_add = Block(next_index, prev_hash, data)
        self.blockchain.add_block(block_to_add)
        return True
    
    def search_for_path(self, path):
        for Block in self.blockchain.chain:
            if Block.data[1] == path:
                return True
            
        return False

    def verify_path(self, path: list):
        """
        This method will take an entry (of the form Block.data) and attempt to form
        and verify the entries path from the blockchain.

        Inputs:
            -path : list [startAS, ..., endAS]
        """
        #Verify the path can be produced from existing secure routers neighbors in blockchain
        path_build = [0 for i in range(len(path)-1)]
        path_build_index = 0
        for asx, asy in zip(path, path[1:]):
            asx_is_secure = False
            link_confirmed = False
            asx_is_secure, link_confirmed = self.confirm_neighbor(asx, asy)
            
            if link_confirmed == True:
                #asx has neighbor asy; mark this link as a real link;
                path_build[path_build_index] = 1
                path_build_index += 1
                #asx = asy; asy = asz; check asx is neighbors with asy
                continue
           
            elif asx_is_secure == True and link_confirmed == False:
                #Then clearly asx does not have a neighbor asy and cannot be verified
                return False
    
            elif asx_is_secure == False:
                #asx is not a secure ebgp router. Must search asy's neighbors for asx
                asy_is_secure, asy_link_conf = self.confirm_neighbor(asy, asx)
                #Now asy must be secure and asx must be a neighbor of asy
                if asy_is_secure and asy_link_conf:
                    path_build[path_build_index] = 1
                    path_build_index +=1
                    continue
                else:
                    #Since there is no way to 100% ensure asx can reach asy the path cant be verified
                    return False
                
        for i in path_build:
            if i == 0:
                return False
        return True

    def confirm_neighbor(self, asx, asy):
        """
        Function to take two as's and confirm whether asx has a neighbor asy
        by checking the blockchain.

        Output: Will output whether asx is a secure router and whether asy 
        is a neighbor of asx
        """
        asx_is_secure = False
        link_confirmed = False
        for block in self.blockchain.chain:
                if block.data[0] != "N":
                    #This means the block is a path update so skip it
                    continue
                
                if block.data[1] == asx:
                    #we have reached the neighbors of asx block
                    asx_is_secure = True
                    for neighbor in block.data[2]:
                        if neighbor == asy:
                            #asx <-> asy confirmed
                            link_confirmed = True
                            break
        return asx_is_secure, link_confirmed
        
    '''
    add neighbors will be called when a AS joins our system. It will create a neighbor block
    and add the block to the blockchain. Requires list of neighbors input.
    '''
    def _add_as_neighbors(self, json_data: str):
        as_list = [n[1] for n in json.loads(json_data)["neighbor_list"]]
        data = ["N", self.as_number, as_list]
        self.write_block_to_blockchain(data)

    '''
    Add an update to the blockchain.
    '''
    def add_path_to_chain(self, prefix, src_as_number, src_ip, as_path):
        data = ["P", prefix, src_as_number, src_ip, as_path]
        self.write_block_to_blockchain(data)

    def _advanced_feature(self, keyword: str, json_data: str):
        if keyword == "neighbor announcement":
            self._add_as_neighbors(json_data)
