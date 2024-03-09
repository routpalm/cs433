from cryptography.hazmat.primitives import serialization

class Certificate:
        # simplified cert with a public key
        def __init__(self, public_key):
            self.public_key = public_key
        def serialize(self):
            # serialize public key to PEM format for storage/transfer
            return self.public_key.public_bytes(
                 encoding=serialization.Encoding.PEM,
                 format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        
class ROA:
    def __init__(self,as_id,ip_addr_blocks, certificate):
          self.as_id = as_id
          self.ip_addr_blocks = ip_addr_blocks
          self.certificate = certificate.serialize().decode()
    def to_dict(self): # needed so we can serialize with json
         return {
            'as_id': self.as_id,
            'ip_addr_blocks': self.ip_addr_blocks,
            'certificate': self.certificate
         }
    def __str__(self):
         return f"AS_ID: {self.as_id}\nIP_ADDR_BLOCKS: {self.ip_addr_blocks}\nCERTIFICATE: {self.certificate}\n"
