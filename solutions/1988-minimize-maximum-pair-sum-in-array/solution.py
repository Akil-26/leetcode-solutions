class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ma = 0
        n = len(nums)
        for i in range(n//2):
            s = nums[i] + nums[len(nums) -1 -i]
            ma = max(ma,s)
        return ma
