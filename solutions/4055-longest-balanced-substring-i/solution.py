class Solution:
    def solve(self, mp):
        mi = float('inf')
        ma = 0
        for val in mp.values():
            mi = min(mi, val)
            ma = max(ma, val)
        return mi == ma

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            mp = {}
            for j in range(i, n):
                mp[s[j]] = mp.get(s[j], 0) + 1
                if self.solve(mp):
                    l = j - i + 1
                    ans = max(ans, l)
        return ans
