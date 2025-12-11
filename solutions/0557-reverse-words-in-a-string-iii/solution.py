class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        res = ""
        for word in st:
            res+=word[::-1]+" "
        return res.strip()
