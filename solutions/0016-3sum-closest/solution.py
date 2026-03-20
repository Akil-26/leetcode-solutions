class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cl = float('inf')
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l < r:
                tot = nums[i]+nums[r]+nums[l]
                if abs(tot-target)<abs(cl-target):
                    cl = tot
                elif tot > target:
                    r-=1
                elif tot < target:
                    l+=1
                else:
                    return tot
        return cl

