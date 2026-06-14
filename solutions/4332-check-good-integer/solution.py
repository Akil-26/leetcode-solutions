class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        dig = [int(i) for i in str(n)]
        sumdig = sum(dig)
        sqdig = sum(i**2 for i in dig)
        return sqdig - sumdig >= 50
