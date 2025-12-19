class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1:
            return s
        pl=2*n-2
        x=pl-2
        res=""
        for i in range(n):
            j=i
            if i==0 or i==n-1:
                while j<len(s):
                    res+=s[j]
                    j+=pl
            else:
                while j<len(s):
                    res+=s[j]
                    if j+x<len(s):
                        res+=s[j+x]
                    j+=pl
                x-=2
        return res
