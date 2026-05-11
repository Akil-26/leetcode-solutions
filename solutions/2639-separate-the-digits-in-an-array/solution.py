class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i>9:
                temp = str(i)
                for j in temp:
                    res.append(int(j))
            else:
                res.append(i)
        return res
