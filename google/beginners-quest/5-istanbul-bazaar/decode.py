from randcrack import RandCrack
import struct

rc = RandCrack()

file = open("robo_numbers_list.txt", "rt").read().replace("-", "")
secret = open("secret.enc", "rb").read()

for f in file.splitlines():
    rc.submit(int(f) - (1 << 31))

flag = ""
for s in secret:
    flag += chr(s ^ rc.predict_getrandbits(8))

print(flag)
