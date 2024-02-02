from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives import hashes
import json
import logging
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
import objects # from objects.py


# assumed formats: public key in decoded PEM format, signature in hex format
def verify_roa(roa, signature):
    try:
        # Verify ROA signature using attached certificate
        serialized_pk = roa['certificate'].encode()
        public_key = load_pem_public_key(serialized_pk)
        return verify_signature(roa, bytes.fromhex(signature), public_key)
    except Exception as e:
        logging.error(f"Failed to verify ROA: {e}")
        return False

def verify_signature(data, signature, public_key):
    try:
        dumped_data = json.dumps(data).encode()
        public_key.verify(
            signature,
            dumped_data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("signature is valid.")
        return True # signature valid
    except Exception as e:
        logging.error(f"signature verification failed, idiot: {e}")
        return False # signature invalid
    
'''
    generate certificate from the public key of private_key
'''
def generate_cert(private_key):
    public_key = private_key.public_key()
    return objects.Certificate(public_key)
'''
    sign the data using private key
''' 
def sign_data(data, private_key):
    signature = private_key.sign(
        json.dumps(data).encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature
