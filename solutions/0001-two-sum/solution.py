from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dec = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dec:
                return [dec[diff],i]
            dec[nums[i]] = i 
