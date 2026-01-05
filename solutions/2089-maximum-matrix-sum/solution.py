class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        tot = 0
        c = 0
        min_abs = float('inf')
        for row in matrix:
            for j in row:
                if j < 0:
                    c^=1 # no need to add the element on count only check its state (0 or 1)
                tot += abs(j)
                min_abs = min(min_abs,abs(j))
        return tot if c == 0 else tot - 2 * min_abs
