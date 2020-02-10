# -*- coding: utf-8 -*-
def to_str(bytes_or_str):
    if not bytes_or_str:
        return bytes_or_str
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(str_to_bytes):
    if not str_to_bytes:
        return str_to_bytes
    if isinstance(str_to_bytes, str):
        value = str_to_bytes.encode('utf-8')
    else:
        value = str_to_bytes
    return value
