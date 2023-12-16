flag = []
with open("step6.txt", "r") as f:
    c = 0
    for line in f.readlines():
        for l in line:
            if l == 'n':
                c -= 1
            if l == 'y':
                c += 1
            if l == 'a':
                flag.append(chr(c))
            if l == '~':
                c = 0

print("".join(flag))
