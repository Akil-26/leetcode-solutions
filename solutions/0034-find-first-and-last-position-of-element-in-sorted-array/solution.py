class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                left = mid
                while left -1 >= 0 and nums[left-1] == target:
                    left-=1
                right = mid
                while right +1 < len(nums) and nums[right+1] == target:
                    right+=1
                return [left,right]
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return [-1,-1]
