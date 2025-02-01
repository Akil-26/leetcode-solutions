class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums) == 1:
            return True
        for i in range(1, len(nums)):  # Start from 1 to compare with the previous element
            if nums[i] % 2 == nums[i - 1] % 2:  # If two consecutive elements are the same parity
                return False
        return True

