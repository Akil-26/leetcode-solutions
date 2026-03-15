"""class Fancy:

    def __init__(self):
        self.res = []
    
    def append(self, val: int) -> None:
        self.res.append(val)
    
    def addAll(self, inc: int) -> None:
        for i in range(len(self.res)):
            self.res[i]+=inc
    
    def multAll(self, m: int) -> None:
        for i in range(len(self.res)):
            self.res[i]*=m
    
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.res):
            return -1
        return self.res[idx]

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)"""

MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        inv = pow(self.mul, MOD-2, MOD)
        stored = (val - self.add) * inv % MOD
        self.seq.append(stored)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % MOD
