from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer
from flask.sessions import SecureCookieSessionInterface, TaggedJSONSerializer
import hashlib


def create_token():
    s = URLSafeSerializer('xxx')
    browser_id = 'ASDF'
    life_time = '100'
    token = s.dumps((1, 'admin', '123456', browser_id, life_time))
    return token


# https://gist.github.com/babldev/502364a3f7c9bafaa6db
def decode_flask_cookie(secret_key, cookie_str):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)


def encode_flask_cookie(secret_key, cookieDict):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt,
                               serializer=serializer,
                               signer_kwargs=signer_kwargs)
    return s.dumps(cookieDict)


secret_key = "CHANGE_ME_TO_A_COMPLEX_RANDOM_SECRET"
if __name__ == '__main__':
    print(decode_flask_cookie(secret_key,
                              ".eJwlz0FqAzEMheG7eD0LSZYsKZcZbI9EQ0IDM8mq9O41dP8-eP9P2fOM66vc3ucntrLfj3IrJmipHjDZjQaLJcLRq0Gi80QS6FgDhxOqmYS7Z28eEsMAhqp2TrURySBM0iZQjgrKPKeLd2ZgwdpSvFbv08wU4wDpk0XLVuZ15v5-PeJ7_QEm6qDVI0N9rbBRw0TuB44WdIhFAuJyz9fsz1hmwa18rjj_k6j8_gH2mEDE.YqgmMg.6zaZu8oS3PoaBCjppn4CATsO4uA"))
    print(encode_flask_cookie(secret_key, {'_fresh': True,
                                           '_id': '8518f79e0c4982b458f10da380f194c1250a13e1b9217885e999fa69e5eb800b777a4f78bef4054256c02fb30744cc959a44045136f59339ac88871ed05ac457',
                                           'csrf_token': '0422a0739efe79d0516261f14ad1b6e2d58ef011', 'locale': 'en',
                                           'user_id': '2'}))

    print(decode_flask_cookie(secret_key,
                              ".eJwkz0Fu60AIANC7sPYCZsCAL2PNMKD_1SiR7GRV9e5d9AjvG8668v4Hx_v65Abn_wUHmJCVemKwW5ssVoRrdMMi56AmOKgnTW-kZpLuXmP3lJyGOFV1cKnNLEbhJntgq9lRmSNcfDAjC_W9xHv3EWamlAtlBIvCBnFfdb5fX_mEA9quOi1kNy_vaSRRXktmlLOtVr5GNinY4PGK8Ug4IJ-wwefO64-E8PMbAAD__yJ6QcA.YqhL6A.XqCq1MDhR6nyIgCltTBLxcIKGGI"))
