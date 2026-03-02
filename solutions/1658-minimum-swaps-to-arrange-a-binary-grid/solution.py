class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = []
        for row in grid:
            count = 0
            for i in reversed(row):
                if i == 0:
                    count+=1
                else:
                    break
            res.append(count)
            
        swap = 0

        for i in range(n):
            req = n-i-1
            j = i
            while j<n and res[j] < req:
                j+=1
            if j == n:
                return -1
            while j > i:
                res[j],res[j-1] = res[j-1],res[j]
                swap += 1
                j -= 1
        return swap
