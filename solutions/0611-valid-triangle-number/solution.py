class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        co = 0
        for k in range(len(nums)-1,1,-1):
            l ,r = 0,k-1
            while l < r:
                if nums[l] + nums[r] > nums[k]:
                    co+= (r - l)
                    r-=1
                else:
                    l+=1
        return co
