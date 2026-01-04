class Solution:
    def sumFourDivisors(self, nums):
        ans = 0
        for n in nums:
            if n < 6:
                continue
            cnt = 2        # 1 and n
            total = 1 + n
            i = 2
            while i * i <= n:
                if n % i == 0:
                    d1, d2 = i, n // i
                    if d1 == d2:
                        cnt += 1
                        total += d1
                    else:
                        cnt += 2
                        total += d1 + d2
                if cnt > 4:
                    break
                i += 1
            if cnt == 4:
                ans += total
        return ans
