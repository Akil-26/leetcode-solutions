class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mapp = {0:-1}
        preSum = 0
        for i in range(len(nums)):
            preSum += nums[i]
            rem = preSum % k
            if rem in mapp:
                if i - mapp[rem] >= 2:
                    return True
            else:
                mapp[rem] = i
        return False
