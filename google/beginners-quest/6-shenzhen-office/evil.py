class EvilInterpreter:
    def __init__(self):
        self.accu: int = 0
        self.wheel: list = []
        self.pental: list = []
        self.source: list = []
        self.markerState: bool = True
        self.wheelPtr: int = 0
        self.pentalPtr: int = 0
        self.sourcePtr: int = 0

    def load_file(self, fname: str):
        with open(fname, "r") as f:
            self.source = f.read()

    def execute(self, cmd: str):
        if cmd == "a":
            self.accu += 1
        elif cmd == "b":
            self.jump(False)
        elif cmd == "c":
            self.insertWheelCell()
        elif cmd == "d":
            self.accu = self.deleteWheelCell(self.accu)
        elif cmd == "e":
            self.accu = self.weave(self.accu)
        elif cmd == "f":
            self.jump(True)
        elif cmd == "g":
            self.accu = self.pental[self.pentalPtr]
        elif cmd == "h":
            self.pentalPtr = (self.pentalPtr + 1) % len(self.pental)
        elif cmd == "i":
            self.wheelPtr = (self.wheelPtr + 1) % len(self.wheel)
        elif cmd == "j":
            pass
        elif cmd == "k":
            self.pental[self.pentalPtr] = self.accu
        elif cmd == "l":
            tmp = self.wheel[self.wheelPtr]
            self.wheel[self.wheelPtr] = self.accu
            self.accu = tmp
        elif cmd == "m":
            pass
        elif cmd == "n":
            self.pentalPtr -= 1
        elif cmd == "o":
            self.wheelPtr -= 1
        elif cmd == "p":
            self.accu = self.wheel[self.wheelPtr]
        elif cmd == "q":
            self.swap()
        elif cmd == "r":
            self.accu = int(input())
        elif cmd == "s":
            if self.accu == 0:
                self.sourcePtr -= 1
        elif cmd == "t":
            if self.accu != 0:
                self.sourcePtr += 1
        elif cmd == "u":
            self.accu -= 1
        elif cmd == "v":
            tmp = self.pental[self.pentalPtr]
            self.pental[self.pentalPtr] = self.accu
            self.accu = tmp
        elif cmd == "w":
            print(chr(self.accu), end="")
        elif cmd == "x":
            self.markerState = ~self.markerState
        elif cmd == "y":
            self.wheel[self.wheelPtr] = self.accu
        elif cmd == "z":
            self.accu = 0

    def jump(self, forward: bool):
        if self.markerState is True:
            mark = "m"
        else:
            mark = "j"
        if forward is True:
            while self.sourcePtr < len(self.source) and self.source[self.sourcePtr] != mark:
                self.sourcePtr += 1
        else:
            while self.sourcePtr >= 0 and self.source[self.sourcePtr] != mark:
                self.sourcePPtr -= 1

    def insertWheelCell(self):
        self.wheel.insert(self.wheelPtr - 1, 0)

    def deleteWheelCell(self):
        del self.wheel[self.wheelPtr]

    def weave(self, cmd: int):
        weaveMap = [4, 1, 16, 2, 64, 8, 128, 32]
        mask = 1
        result = 0
        for i in range(0, 8):
            if ((cmd & mask) != 0):
                result |= weaveMap[i]
            mask = mask << 1
        return result

    def swap(self):
        tmp = self.wheel
        self.wheel = self.source
        self.source = tmp
        tmp = self.wheelPtr
        self.wheelPtr = self.sourcePtr
        self.sourcePtr = tmp

    def run(self):
        while self.sourcePtr < len(self.source):
            self.execute(self.source[self.sourcePtr])
            self.sourcePtr += 1


evil = EvilInterpreter()
evil.load_file("step2.txt")
evil.run()