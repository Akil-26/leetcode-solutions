class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def qu(cur,open,close):
            if len(cur) == 2*n:
                res.append(cur)
                return
            if open < n :
                qu(cur+"(",open+1,close)
            if close < open:
                qu(cur+")",open,close+1)
        qu("",0,0)
        return res
