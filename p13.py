import hashlib
import itertools

init = b'c'
h = 'd077f244def8a70e5ea758bd8352fcd8'

chars = [i for i in range(256)]

for cs in itertools.product(*[chars] * 2):
    s = init + bytes(cs)
    if hashlib.new('md5', s).hexdigest() == h:
        print(s)

for c1 in 'cau':
    for c2 in 'cas':
        print(c1 + c2)

# jwt/claims_auth.py
import jwt
data = {'payload': 'data', 'iss': 'Headquarters', 'aud': 'learn-python'}
secret = 'secret-key'
token = jwt.encode(data, secret)
def decode(token, secret, issuer=None, audience=None):
    try:
        print(jwt.decode(token, secret, issuer=issuer,
                         audience=audience, algorithms=["HS256"]))
    except (
        jwt.InvalidIssuerError, jwt.InvalidAudienceError
    ) as err:
        print(err)
        print(type(err))
decode(token, secret)
# not providing the issuer won't break
decode(token, secret, audience='learn-python')
# not providing the audience will break
decode(token, secret, issuer='Headquarters')
# both will break
decode(token, secret, issuer='wrong', audience='learn-python')
decode(token, secret, issuer='Headquarters', audience='wrong')
decode(token, secret, issuer='Headquarters', audience='learn-python')
