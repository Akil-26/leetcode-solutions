class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = ""
        v = abs(num)
        while v > 0:
            res += str(v%7)
            v=v//7
        return "-"+res[::-1] if num < 0 else res[::-1]
