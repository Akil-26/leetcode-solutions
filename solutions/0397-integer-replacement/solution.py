class Solution:
    def integerReplacement(self, n: int) -> int:
        def dp(i, memo: dict):
            if i == 1:
                return 0
            if i not in memo:
                if i % 2 == 0:
                    memo[i] = 1 + dp(i / 2, memo)
                else:
                    memo[i] = 1 + min(dp(i+1, memo), dp(i-1, memo))
            return memo[i]
        return dp(n, {})
