import struct
import base64

f = open("hideandseek.png", "rb").read()

header = f[:8]
chunks = f[8:]

print(f[1:4])

flag = ""
i = 0
len_chunks = len(chunks)
while i < len_chunks :
    len = struct.unpack(">I", chunks[i:i+4])[0]
    type = chunks[i+4:i+8]
    data = chunks[i+8:i+8+len]
    if type == bytes("eDIH".encode()):
        flag += data.decode()
    i += 8 + len + 4

print(base64.b64decode(flag))
