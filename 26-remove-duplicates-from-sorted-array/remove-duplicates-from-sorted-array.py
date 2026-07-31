class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        v1 = 0
        for v2 in range(1,len(nums)):
            if nums[v1] != nums[v2]:
                v1+=1
                nums[v1],nums[v2] = nums[v2],nums[v1]
        return v1+1