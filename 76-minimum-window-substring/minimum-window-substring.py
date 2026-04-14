class Solution:
    def minWindow(self, s: str, t: str) -> str:
        Tcount , window = {} , {}
        for ch in t:
            Tcount[ch] = Tcount.get(ch,0) + 1
        res , reslen = [-1,-1] , float('inf')
        have , need = 0 , len(Tcount)
        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch,0) + 1
            if ch in Tcount and window[ch] == Tcount[ch]:
                have += 1
            while have == need:
                if (right - left + 1) < reslen:
                    res = [left,right]
                    reslen = right - left + 1
                window[s[left]] -= 1
                if s[left] in Tcount and window[s[left]] < Tcount[s[left]]:
                    have -= 1
                left += 1
        left , right = res
        return s[left : right + 1] if reslen != float('inf') else ''