
msg = []
with open("step7.txt", "rt") as f:
    b = bin(int(f.read()))[2::]

    for c in range(1, len(b), 3):
        k = b[c:c+3]

        if k == "000":
            msg.append(">")
        if k == "001":
            msg.append("<")
        if k == "010":
            msg.append("+")
        if k == "011":
            msg.append("-")
        if k == "100":
            msg.append(".")
        if k == "101":
            msg.append(",")
        if k == "110":
            msg.append("[")
        if k == "111":
            msg.append("]")

msg = "".join(msg)
print(msg)
with open("step8.txt", "wt") as f:
    f.write(msg)


"""

>	000
<	001
+	010
-	011
.	100
,	101
[	110
]	111

"""
