import hashlib
import pickle

import log

# list of algorithms and their names
algorithms = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}

# read the password hash from the given file
with open('password.dat', 'rb') as f:
    password_hash = pickle.load(f)

print(f'The password hash from password.dat is: {repr(password_hash)}')

successes = [] # list of matching passwords

for i in range(10000):
    password = str(i).zfill(4) # pad the password to 4 digits
    for hash_name,hash_algorithm in algorithms.items():
        log.log_attempt(password, hash_name)
        hashed_password = hash_algorithm(bytes(password, 'utf-8')).digest().hex()
        if hashed_password == password_hash: # check the hash
            log.log_success(password, hash_name)
            successes.append((password, hash_name)) # add this password and hash function to the list of matching passwords

# output
print('Possible passwords and hash functions:')
for password,hash_name in successes:
    print(f'  Password: {repr(password)}  Hash: {hash_name}')