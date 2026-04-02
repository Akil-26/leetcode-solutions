class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = [0]*len(nums)
        for i in range(len(nums)):
            v = nums[i]**2
            sq[i] = v
        sq.sort()
        return sq
