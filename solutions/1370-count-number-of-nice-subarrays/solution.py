class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        c = 0
        preSum = 0
        mapp = {0:1}
        for num in nums:
            if num % 2 == 1:
                preSum += 1
            else:
                preSum += 0
            if preSum-k in mapp:
                c += mapp[preSum-k]
            mapp[preSum] = mapp.get(preSum,0) + 1
        return c
