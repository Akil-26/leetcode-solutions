class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [0] * n
        val = 1
        for i in range(n):
            if s[i] > 0:
                continue
            if val > 26:
                return ""
            for j in range(i, n):
                if lcp[i][j] > 0:
                    s[j] = val
            val += 1
        res = "".join(chr(ord('a') + i - 1) for i in s)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                new = 0
                if res[i] == res[j]:
                    new = 1
                    if i + 1 < n and j + 1 < n:
                        new += lcp[i + 1][j + 1]
                if lcp[i][j] != new:
                    return ""
        return res

