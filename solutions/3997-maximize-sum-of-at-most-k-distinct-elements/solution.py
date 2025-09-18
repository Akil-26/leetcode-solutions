class Solution:
    def maxKDistinct(self, nums, k):
        distinct = list(set(nums))
        distinct.sort(reverse=True)
        return distinct[:k]
