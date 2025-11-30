class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0
        prefix = 0
        seen = {0: -1}
        ans = len(nums)
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p
            target = (prefix - need) % p
            if target in seen:
                ans = min(ans, i - seen[target])
            seen[prefix] = i
        return ans if ans < len(nums) else -1
