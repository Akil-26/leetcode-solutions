class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        c = 0
        preSum = 0
        mapp = {0:1}
        for num in nums:
            preSum += num
            if preSum-k in mapp:
                c += mapp[preSum-k]
            mapp[preSum] = mapp.get(preSum,0) + 1
        return c
