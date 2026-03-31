class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        dic = {0:1}
        pre = 0
        for num in nums:
            pre += num
            if pre-k in dic:
                c += dic[pre-k]
            dic[pre] = dic.get(pre,0) + 1
        return c
