class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temp[j] <= temp[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i
        return res