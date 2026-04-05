class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k]) 
        max_av = window
        for i in range(k,len(nums)):
            window += nums[i]
            window -= nums[i-k]
            max_av = max(max_av,window)
        return max_av/k
