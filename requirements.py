
import hashlib

def hash_string(string):
    
    hash_object = hashlib.sha256()

    
    hash_object.update(string.encode('utf-8'))

    
    hashed_string = hash_object.hexdigest()

    return hashed_string
