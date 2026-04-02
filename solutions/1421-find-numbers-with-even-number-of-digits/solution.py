class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        final = 0
        res = []
        def find(num):
            c = 0
            if num == 0:
                return res.append(0)
            while num > 0:
                num //= 10
                c+=1
            return res.append(c)
        for i in range(len(nums)):
            find(nums[i])
            if res[i]%2 ==0:
                final += 1
        return final
