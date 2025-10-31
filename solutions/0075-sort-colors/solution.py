class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1,len(nums)):
            cur = nums[i]
            j = i-1
            while j>=0 and cur < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = cur
        return nums
