class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def bt(i,summ):
            if i == len(nums):
                return 1 if summ == target else 0
            if (i,summ) in memo:
                return memo[(i,summ)]
            add = bt(i+1,summ+nums[i])
            sub = bt(i+1,summ-nums[i])
            memo[(i,summ)] = add+sub
            return memo[(i,summ)]
        return bt(0,0)
