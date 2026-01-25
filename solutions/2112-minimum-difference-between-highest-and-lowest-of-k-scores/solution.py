class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        m_diff = float('inf')
        
        for i in range(len(nums) - k + 1):
            m_diff = min(m_diff, nums[i + k - 1] - nums[i])
        
        return m_diff
