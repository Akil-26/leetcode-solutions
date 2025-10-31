class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dec = {}
        for i in range(len(nums)):
            deff = target-nums[i]
            if deff in dec:
                return [dec[deff],i]
            dec[nums[i]] = i
