class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_= nums[0]
        min_= nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            temp = max_
            max_ = max(nums[i], nums[i] * max_, nums[i] * min_)
            min_ = min(nums[i], nums[i] * temp, nums[i] * min_)
            res = max(res, max_)
        return res