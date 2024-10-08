
import hashlib

def hash_string(string):
    
    hash_object = hashlib.sha256()

    
    hash_object.update(string.encode('utf-8'))

    # Get the hashed string in hexadecimal form
    hashed_string = hash_object.hexdigest()

    return hashed_string
