class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            c_sum = 0
            seen = set()
            for j in range(i,n):
                c_sum += nums[j]
                seen.add(nums[j])
                if c_sum in seen:
                    ans += 1
        return ans
