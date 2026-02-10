class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for j in range(n):
            set_e = set()
            set_o = set()
            for i in range(j,n):
                if nums[i] % 2 == 0:
                    set_e.add(nums[i])
                else:
                    set_o.add(nums[i])
                if len(set_e) == len(set_o):
                    res = max(res,i-j+1)
        return res
