class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            current_sum = num if current_sum < 0 else current_sum + num
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
