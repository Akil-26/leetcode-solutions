class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        prev = 0
        for num in nums:
            curr_sum = max(num,num+prev)
            result = max(result,curr_sum)
            prev = curr_sum
        return result