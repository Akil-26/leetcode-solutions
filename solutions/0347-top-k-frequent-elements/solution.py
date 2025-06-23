class Solution:
    def topKFrequent(self, nums, k):
        co = Counter(nums)
        heap = []
        for i, j in co.items():
            heapq.heappush(heap, (j, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
