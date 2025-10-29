import logging

logger = logging.getLogger('hash_solve.log')
logger.setLevel(logging.DEBUG)

logging.basicConfig(
    stream = open('hash_log.log', 'w'),
    level = logging.INFO,
    format = '[%(asctime)s] %(levelname)s: %(message)s',
    datefmt = '%m/%d/%Y %I:%M:%S %p',
)

def log_attempt(password, hash_name):
    # log entry for an attempt
    logger.debug(f'ATTEMPT: Trying password {repr(password)} with hash algorithm {hash_name}')

def log_success(password, hash_name):
    # log entry for a success
    logger.info(f'SUCCESS: {repr(password)} with hash algorithm {hash_name} matches the given hash')