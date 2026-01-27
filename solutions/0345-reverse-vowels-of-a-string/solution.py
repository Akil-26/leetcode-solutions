class Solution:
    def reverseVowels(self, s: str) -> str:
        copy = list(s)
        vow = 'aeiouAEIOU'
        l = 0
        r = len(s)-1
        while l < r:
            while l < r and copy[l] not in vow:
                l += 1
            while l < r and copy[r] not in vow:
                r -= 1
            copy[l],copy[r] = copy[r],copy[l]
            l += 1
            r -= 1
        return "".join(copy)
