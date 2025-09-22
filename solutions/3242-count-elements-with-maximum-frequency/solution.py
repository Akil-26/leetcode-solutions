from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        mc = max(c.values())
        res = 0
        for i, (num,cont) in enumerate(c.items()):
            if cont == mc:
                res += cont
        return res 
