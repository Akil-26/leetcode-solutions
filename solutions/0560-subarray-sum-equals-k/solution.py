class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        summ = 0
        dic = {0:1}
        for num in nums:
            summ += num
            if summ-k in dic:
                c += dic[summ-k]
            dic[summ] = dic.get(summ,0)+1
        return c
