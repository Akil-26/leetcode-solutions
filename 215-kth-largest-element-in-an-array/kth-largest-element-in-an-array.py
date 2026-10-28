class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        for _ in range(k-1):
            heapq.heappop(max_heap)
        return -heapq.heappop(max_heap)