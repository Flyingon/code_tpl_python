# -*- coding: UTF-8 -*-
# ! /usr/bin/env python
import base64
import rsa
from rsa import common

pub_path = "/xxx/client.pub"
private_path = "/xxx/client.pem"

with open(private_path, mode='rb') as privatefile:
    priv_keydata = privatefile.read()
priv_key = rsa.PrivateKey.load_pkcs1(priv_keydata)
with open(pub_path, mode='rb') as pubfile:
    pub_keydata = pubfile.read()
pub_key = rsa.PublicKey.load_pkcs1(pub_keydata)

test_msg = b"DOGDOG"
encoded_str = rsa.encrypt(message=test_msg, pub_key=pub_key)
print(encoded_str)
