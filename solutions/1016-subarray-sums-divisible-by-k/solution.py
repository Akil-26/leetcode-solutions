class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = 0
        su = 0
        dic = {0:1}
        for num in nums:
            su += num
            rem = su%k
            if rem<0:
                continue
            if rem in dic:
                c+= dic[rem]
            dic[rem] = dic.get(rem,0)+1
        return c
