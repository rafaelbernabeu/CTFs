
for i in range(1,8):
    w = []
    x = []
    y = []
    z = []
    with open(f"{i}.csv", "r") as f:
        lines = f.read().splitlines()
        for l in lines:
            d = l.split(",")
            w.append(float(d[0]))
            x.append(float(d[1]))
            y.append(float(d[2]))
            z.append(float(d[3]))

        for arr in [w,x,y,z]:
            minimo = min(arr)
            maximo = max(arr) - minimo
            for j in range(len(arr)):
                arr[j] += -minimo
                arr[j] *= 255/maximo

        with open(f"w_{i}.data", "wb") as s:
            s.write(bytes([int(q) for q in w]))

        with open(f"x_{i}.data", "wb") as s:
            s.write(bytes([int(q) for q in x]))

        with open(f"y_{i}.data", "wb") as s:
            s.write(bytes([int(q) for q in y]))

        with open(f"z_{i}.data", "wb") as s:
            s.write(bytes([int(q) for q in z]))
