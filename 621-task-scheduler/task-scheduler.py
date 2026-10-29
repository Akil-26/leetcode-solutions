from collections import Counter,deque
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        Taskfreq = Counter(tasks)
        heap = [-x for x in Taskfreq.values()]
        
        heapq.heapify(heap)
        q = deque()
        time = 0

        while q or heap:
            if q and q[0][1] <= time:
                count , t = q.popleft()
                heapq.heappush(heap,count)
            if heap:
                count = heapq.heappop(heap)
                count += 1

                if count < 0:
                    q.append((count,time + n + 1))
                
            time += 1
        return time