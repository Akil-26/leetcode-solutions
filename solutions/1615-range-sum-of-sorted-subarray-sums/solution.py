import heapq
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        heap = []
        for i in range(n):
            heapq.heappush(heap, (nums[i], i))
        ans = 0
        for k in range(1, right + 1):
            curr_sum, idx = heapq.heappop(heap)
            if k >= left:
                ans = (ans + curr_sum) % MOD
            if idx + 1 < n:
                heapq.heappush(heap, (curr_sum + nums[idx + 1], idx + 1))
        return ans
