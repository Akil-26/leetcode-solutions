from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def find_peak(left, right):
            if left == right:
                return left
            
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid + 1]:
                return find_peak(mid + 1, right)
            else:
                return find_peak(left, mid)
        
        return find_peak(0, len(nums) - 1)

