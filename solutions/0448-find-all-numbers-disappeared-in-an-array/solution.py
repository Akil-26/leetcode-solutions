class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        li = [x for x in range(1,len(nums)+1)]
        s=set(li)-set(nums)
        return list(s)
