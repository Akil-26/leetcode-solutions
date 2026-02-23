class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        tar = 1 << k
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
            if len(seen) == tar:
                return True
        return len(seen) == tar
