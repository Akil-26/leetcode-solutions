class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1 , max(piles)
        res = right
        while left <= right:
            k = left + (right-left) // 2
            curr_hrs = 0
            for pile in piles:
                curr_hrs += math.ceil(float(pile)/k) # ceil for round the values
            if curr_hrs <= h:
                res = k
                right = k-1
            else:
                left = k+1
        return res
