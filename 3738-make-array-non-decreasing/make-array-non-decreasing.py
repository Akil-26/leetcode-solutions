class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        maxs = 0
        curr = -1
        for i in nums:
            if i >= curr:
                maxs += 1
                curr = i
        return maxs