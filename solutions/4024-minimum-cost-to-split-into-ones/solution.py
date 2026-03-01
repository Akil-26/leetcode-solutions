class Solution:
    def minCost(self, n: int) -> int:
        v = n
        return v*(v-1)//2
