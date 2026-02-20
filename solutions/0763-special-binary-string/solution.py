class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        co = 0
        st = 0
        res = []
        for end in range(len(s)):
            co += 1 if s[end] == '1' else -1
            if co == 0 :
                res.append('1' + self.makeLargestSpecial(s[st+1:end]) + '0')
                st=end+1
        res.sort(reverse=True)
        return ''.join(res)
