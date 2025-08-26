class Solution:
    def addDigits(self, num: int) -> int:
        res = str(num)
        st = True
        while st :
            if len(res) == 1:
                st = False
                return int(res)
            else:
                ad = [int(n) for n in res]
                res = str(sum(ad))
