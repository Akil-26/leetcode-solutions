class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        C = Counter(nums)
        res = []
        limit = len(nums)//3
        for val,c in C.items():
            if c >limit:
                res.append(val)
        return res
