from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nums = nums[:]  # work on copy
        operations = 0
        
        while len(nums) > 1:
            # Check if already non-decreasing
            is_non_decreasing = True
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    is_non_decreasing = False
                    break
            
            if is_non_decreasing:
                return operations
            
            # Find leftmost pair with minimum sum
            min_sum = float('inf')
            merge_idx = -1
            
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum or (current_sum == min_sum and i < merge_idx):
                    min_sum = current_sum
                    merge_idx = i
            
            # Perform the merge
            nums[merge_idx] += nums[merge_idx + 1]
            del nums[merge_idx + 1]
            operations += 1
        
        return operations
