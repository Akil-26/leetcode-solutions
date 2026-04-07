class Solution(object):
    def reverseStr(self, s, k):
        i = 0
        while i < len(s):
            s = s[:i] + s[i:i+k][::-1] + s[i+k:]
            i = i + 2*k
        return s
