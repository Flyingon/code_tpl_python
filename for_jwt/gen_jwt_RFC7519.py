# https://pyjwt.readthedocs.io/en/stable/index.html

import jwt
import time
import uuid

with open("/xxx/client.pem", "rb") as f:
    private_key = f.read()
with open("/xxx/client.pub", "rb") as f:
    public_key = f.read()
print(private_key)
print(public_key)

client_id = "xxx"
key_id = "xxx"

encoded_jwt = jwt.encode({
    "iss": client_id,
    "sub": client_id,
    "jti": str(uuid.uuid4()),
    "exp": int(time.time()) + 60 * 60 * 24 * 365,
    "aud": 'xxx'
}, private_key, algorithm="RS256",
    headers={'alg': 'RS256', 'typ': 'JWT', 'kid': key_id})

print(encoded_jwt)

