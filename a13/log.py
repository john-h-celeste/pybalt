import time

log_file = open('hash_log.log', 'w')

def log(message):
    # log a message with a time
    log_file.write(f'[{time.asctime()}] {message}\n')

def log_attempt(password, hash_name):
    # log entry for an attempt
    log(f'ATTEMPT: Trying password {repr(password)} with hash algorithm {hash_name}')

def log_success(password, hash_name):
    # log entry for a success
    log(f'SUCCESS: {repr(password)} with hash algorithm {hash_name} matches the given hash')