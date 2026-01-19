class Solution:
    def maxSideLength(self, mat, threshold):
        m = len(mat)
        n = len(mat[0])
        # Step 1: Build prefix sum matrix
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i+1][j+1] = mat[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]
        # Function to check if any k x k square is valid
        def check(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    square_sum = (
                        pre[i][j]
                        - pre[i-k][j]
                        - pre[i][j-k]
                        + pre[i-k][j-k]
                    )
                    if square_sum <= threshold:
                        return True
            return False
        # Step 2: Binary search on side length
        low, high = 1, min(m, n)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1   # try bigger square
            else:
                high = mid - 1  # try smaller square
        return ans
