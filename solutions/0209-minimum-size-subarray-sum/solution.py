class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        l = 0
        res = []
        sub_sum = 0
        while r < len(nums):
            sub_sum += nums[r]
            while sub_sum >= target:
                res.append(r-l+1)
                sub_sum -= nums[l]
                l+=1
            r+=1
        return min(res) if res else 0
