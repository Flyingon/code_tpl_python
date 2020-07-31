import os
import platform
import socket
import random
import gzip
import json
import requests as req
from urllib.parse import quote
import xxtea
import logging
import base64
import hmac
from hashlib import sha1


def hash_hmac_base64(code, key, sha1):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1).digest()
    print(hmac_code)
    return base64.b64encode(hmac_code).decode()


def create_sign(method, url_path, params, secret):
    if "sig" in params:
        del params["sig"]
    strs = "%s&%s&" % (method.upper(), quote(url_path, safe=""))
    keys = sorted(  params.keys())
    query_str_list = []
    for k in keys:
        query_str_list.append("%s=%s" % (k, params[k]))
    query_str = "&".join(query_str_list)
    mk = strs + quote(query_str, safe="").replace("~", '%7E')
    print(mk)
    secret = secret.replace("-", "+").replace("_", "/")
    print(secret)
    return hash_hmac_base64(mk, secret, sha1)


if __name__ == '__main__':
    # print(create_sign("POST", "/api/getAllUnreadNumForApI", {"appid": "1000001", "gameId": "107"},
    #                   "kRpKaAyrgDXBm7gOP3p4z6uE4eTFPZiz&"))

    print(create_sign("POST", "/book/api/getAssets", {'userId': '54523', 'osType': 2, 'appid': '1000001', 'token': 'bXDaBN4C'},
                      "kRpKaAyrgDXBm7gOP3p4z6uE4eTFPZiz&"))

