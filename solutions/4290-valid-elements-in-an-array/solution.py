class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums)<=1:
            return nums
            
        valid = [False] * len(nums)
        
        valid[0] = True
        cur = nums[0]
        for i in range(1,len(nums)):
            if cur < nums[i]:
                cur = nums[i]
                valid[i] = [True]
        cur = nums[-1]
        valid[-1] = [True]
        for i in range(len(nums)-2,-1,-1):
            if cur < nums[i]:
                cur = nums[i]
                valid[i] = [True]
        return [nums[i] for i in range(len(nums)) if valid[i]]
