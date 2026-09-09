class Solution:
    def countCommas(self, n: int) -> int:
        tot = 0
        p = 1000
        while p <= n:
            tot += n - p + 1
            p *= 1000
        return tot