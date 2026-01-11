class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        res = 0
        for i,n in enumerate(s):
            seen.add(n)
            if len(seen) == (i+1) % 3:
                res +=1
        return res
