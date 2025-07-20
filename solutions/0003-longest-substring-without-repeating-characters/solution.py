class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i =  0
        length = 0
        for j in range(len(s)):
            while s[j] in s[i:j]:
                i += 1
            length = max(length, j - i + 1)
        return length
