import time

log_file = open('hash_log.log', 'w')

def log(message):
    log_file.write(f'[{time.asctime()}] {message}\n')

def log_attempt(password, hash_name):
    log(f'ATTEMPT: Trying password {password} with hash algorithm {hash_name}')

def log_success(password, hash_name):
    log(f'SUCCESS: {password} with hash algorithm {hash_name} matches the given hash')