class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            val = 0
            for v in str(i):
                val += int(v)
            res.append(val)
        min_v = float('inf')
        for i in res:
            if i < min_v:
                min_v = i
        return min_v
