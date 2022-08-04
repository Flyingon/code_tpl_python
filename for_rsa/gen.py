# https://stuvel.eu/python-rsa-doc/usage.html#encryption-and-decryption

import rsa

(pubkey, privkey) = rsa.newkeys(512)

print(pubkey)
print(privkey)
