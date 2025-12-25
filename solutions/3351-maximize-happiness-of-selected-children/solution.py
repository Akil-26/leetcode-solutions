class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i in range(k):
            total = happiness[i] - i
            if total>0:
                res += total
        return res
