class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            larg_1 = -heapq.heappop(max_heap)
            larg_2 = -heapq.heappop(max_heap)

            if larg_1 != larg_2:
                heapq.heappush(max_heap,larg_2 - larg_1)
        
        return -max_heap[0] if max_heap else 0