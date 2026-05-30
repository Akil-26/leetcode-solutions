class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res =  [[n*n]]
        lo = n*n
        while lo > 1:
            res = [list(r) for r in zip(*res[::-1])]
            cols = len(res[0])
            lo-=cols
            res.insert(0,list(range(lo,lo+cols)))
        return res
