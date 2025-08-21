import hashlib

import log

algorithms = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}

password_hash = hashlib.md5(b'3674').digest()

successes = []

for i in range(10000):
    password = bytes(str(i).zfill(4), 'utf-8')
    for hash_name,hash_algorithm in algorithms.items():
        log.log_attempt(password, hash_name)
        hashed_password = hash_algorithm(password).digest()
        if hashed_password == password_hash:
            log.log_success(password, hash_name)
            successes.append((password, hash_name))

print(successes)