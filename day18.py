# hashlib
# secrets
# json web tokens (jwt)

# PyCryptodome
# Cryptography
# PyNaCl
# PyOpenSSL
# Frenet
# Keyczar
# M2Crypo
# Asn1crypo
# PyJWT

# me when obfuscation using base64
# "base64 is encryption" ahh professor

# encryption is making a message unreadable except by the reciever

import base64 
str_ = "AB"
str_bytes = str_.encode("ascii") 
b64_bytes = base64.b64encode(str_bytes) 
new64_string = b64_bytes.decode("ascii") 
print(f"New encoded string: {new64_string}") 

import hashlib
print(hashlib.algorithms_available)

import hashlib
h = 'professor'
print(hashlib.new('md5', h.encode('UTF-8')).hexdigest())
print(hashlib.new('md5', b'professor').hexdigest())

# there is no one hashing exists for two data
# my man when he finds out about hash collisions:

# jwts
# header.payload.signature
# all base64url encoded (no padding, -_ instead of +/)

# payload is unencrypted <3

# jwt/tok.py
import jwt
jwti = jwt.JWT()
makekey = lambda x: jwt.jwk_from_dict({'kty': 'oct', 'k': x})
data = {'payload': 'data', 'id': 123456789}
token = jwti.encode(data, makekey('secret-key'))
print(f'The token is \n{token}\n')
algs = ['HS256', 'HS512']
data_out = jwti.decode(token, makekey('secret-key'), algorithms=algs)
print(data_out)
