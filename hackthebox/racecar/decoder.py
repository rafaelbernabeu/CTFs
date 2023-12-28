flag = "0x5662896c 0x580151c0 0x58015340 0x7b425448 0x5f796877 0x5f643164 0x34735f31 0x745f3376 0x665f3368 0x5f67346c 0x745f6e30 0x355f3368 0x6b633474 0x7d213f 0x94ab8100 0xf7f663fc 0x5662af8c 0xff853548 0x56628441 0x1 0xff8535f4 0xff8535fc 0x94ab8100 0xff853560"

flag = flag.replace("0x", "")

print(flag)
print("\n")

decoded = ""
for byte_string in flag.split(" "):
    bLen = len(byte_string)
    decoding = []
    for i in range(0, bLen, 2):
        decoding.append(chr(int(byte_string[i:i+2], 16)))
    decoding.reverse()
    decoded += "".join(decoding)

print(decoded)