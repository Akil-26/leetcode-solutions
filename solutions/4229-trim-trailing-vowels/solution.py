class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        for i in range(len(s)-1,-1,-1):
            if s[i] not in 'aeiou':
                return s[:i+1]
        return ""
