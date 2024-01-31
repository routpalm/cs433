from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import json

def verify_roa(roa, signature):
    # Verify ROA signature using attached certificate
    serialized_pk = roa['certificate'].encode()
    public_key = load_pem_public_key(serialized_pk)
    return verify_signature(roa, bytes.fromhex(signature), public_key)

def verify_signature(data, signature, public_key):
    try:
        public_key.verify(
            signature,
            json.dumps(data,sort_keys=True).encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True # signature valid
    except Exception as e:
        return False # signature invalid