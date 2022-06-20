from hashlib import sha512


def _create_identifier(remote_addr, user_agent):
    base = '{0}|{1}'.format(remote_addr.encode(), user_agent.encode())
    if str is bytes:
        base = str(base, 'utf-8', errors='replace')  # pragma: no cover
    print(base.encode('utf8'))
    h = sha512()
    h.update(base.encode('utf8'))
    return h.hexdigest()


if __name__ == '__main__':
    print(_create_identifier("127.0.0.1",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"))
