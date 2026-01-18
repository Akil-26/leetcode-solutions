class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vov = set('aeiou')
        v = c = 0
        for i in s:
            if i.isalpha():
                if i in vov:
                    v+=1
                else:
                    c+=1
        return v//c if c > 0 else 0
