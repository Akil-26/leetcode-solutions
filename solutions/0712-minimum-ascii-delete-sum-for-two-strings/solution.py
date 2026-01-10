class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        # Always keep s2 as the shorter string (optional but good)
        if m > n:
            s1, s2 = s2, s1
            n, m = m, n
        prev = [0] * (m + 1)
        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + ord(s1[i - 1])
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        total1 = sum(ord(c) for c in s1)
        total2 = sum(ord(c) for c in s2)
        return total1 + total2 - 2 * prev[m]
