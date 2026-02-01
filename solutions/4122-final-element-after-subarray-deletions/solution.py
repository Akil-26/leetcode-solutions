from typing import List

class Solution:
    def finalElement(self, nums: List[int]) -> int:   
        n = nums  
        
        if len(n) == 0:
            return 0              
        return max(n[0], n[-1])
