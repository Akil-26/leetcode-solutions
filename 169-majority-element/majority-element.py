class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums)//2
        dic = {}
        for v in nums:
            dic[v] = dic.get(v,0)+1
        for key,value in dic.items():
            if value > k:
                return key