class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx1 = 0
        for idx2 in range(len(nums)):
            if nums[idx2] != 0:
                nums[idx1],nums[idx2] = nums[idx2],nums[idx1]
                idx1 += 1
        return nums