class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.strip().split()
        res= ""
        for i in range(len(s)-1,-1,-1):
            res+=s[i]+" "
        return res.strip()
