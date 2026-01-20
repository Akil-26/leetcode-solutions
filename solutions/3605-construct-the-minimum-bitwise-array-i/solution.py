class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if i % 2 == 0:
                ans.append(-1)
                continue
            k = 0
            temp = i
            while temp & 1:
                k+=1
                temp >>=1
            ans.append(i - (1 << (k-1)))
        return ans
