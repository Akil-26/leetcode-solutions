class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        tot = 0
        left = 0
        mim = len(nums)+1

        for right in range(len(nums)):
            tot += nums[right]

            while tot >= target:
                length = right - left + 1
                mim = min(mim,length)

                tot -= nums[left]
                left += 1
        return 0 if mim == len(nums) + 1 else mim