class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = nums * 2
        for i in range(len(nums)):
            if i == 0:
                ans[-1] = ans[0]
            ans[-(i+1)] = ans[i]
        return ans
