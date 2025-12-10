class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre = {}
        for i in s:
            fre[i] = fre.get(i,0)+1
        for i in range(len(s)):
            if fre[s[i]] == 1:
                return i
        return -1
