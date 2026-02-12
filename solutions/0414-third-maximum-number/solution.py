class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) <= 2:
            return max(nums)
        for i in range(3):
            res = max(nums)
            nums.remove(res)
        return res
