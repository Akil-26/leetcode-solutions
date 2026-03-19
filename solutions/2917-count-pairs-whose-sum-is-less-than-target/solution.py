class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l,r =0,len(nums)-1
        co = 0
        while l < r:
            tot = nums[l]+nums[r]
            if tot < target:
                co += (r-l)
                l+=1
            else:
                r-=1
        return co

