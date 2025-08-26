import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n<1): return False
        res = math.log10(n)/math.log10(4)
        return res - int(res) == 0
