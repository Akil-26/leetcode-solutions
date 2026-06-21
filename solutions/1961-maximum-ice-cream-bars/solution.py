class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c = 0
        for i in costs:
            if i <= coins:
                c+=1
                coins -= i
            else:
                break
        return c
