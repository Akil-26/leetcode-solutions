class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        gap = 0
        prev = -6
        for i in range(len(b)):
            if b[i] == "1":
                if prev != -6:
                    gap = max(gap,i-prev)
                prev = i
        return gap
