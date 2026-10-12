"""Cryptographic helpers"""

import hashlib
from typing import Union

def sha256(data: Union[bytes, str]) -> bytes:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).digest()

def ripemd160(data: bytes) -> bytes:
    h = hashlib.new("ripemd160")
    h.update(data)
    return h.digest()

def hash160(data: bytes) -> bytes:
    return ripemd160(sha256(data))
