from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
import json
import objects # from objects.py
import ROAservertest

'''
    ROAclienttest.py
    This shows what the ROA creation process looks like for a network operator.
    General flow -> create key pair -> enter info into ROA (asn, prefixes) -> sign ROA
'''


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

# generate a private key & cert
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
cert = generate_cert(private_key)

# example roa
roa= objects.ROA(12345, [{'address': '192.168.0.0', 'max_length': 24}],cert)
signature = sign_data(roa, private_key).hex()
print("ROA:", roa)
print(ROAservertest.verify_roa(roa,signature=signature))
