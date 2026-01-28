import heapq
from typing import List
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18
        
        # dist[i][j][t] = min cost to reach (i,j) using t teleports
        dist = [[[INF] * (k+1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0
        
        pq = [(0, 0, 0, 0)]  # cost, i, j, t
        
        # all cells sorted by value
        cells = sorted(
            (grid[i][j], i, j) for i in range(m) for j in range(n)
        )
        
        # used[t] = how many cells already unlocked for teleport count t
        used = [0] * (k+1)
        
        while pq:
            cost, i, j, t = heapq.heappop(pq)
            
            if cost > dist[i][j][t]:
                continue
            
            # normal moves
            if i + 1 < m:
                nc = cost + grid[i+1][j]
                if nc < dist[i+1][j][t]:
                    dist[i+1][j][t] = nc
                    heapq.heappush(pq, (nc, i+1, j, t))
            
            if j + 1 < n:
                nc = cost + grid[i][j+1]
                if nc < dist[i][j+1][t]:
                    dist[i][j+1][t] = nc
                    heapq.heappush(pq, (nc, i, j+1, t))
            
            # teleport moves
            if t < k:
                while used[t] < len(cells) and cells[used[t]][0] <= grid[i][j]:
                    _, x, y = cells[used[t]]
                    used[t] += 1
                    
                    if cost < dist[x][y][t+1]:
                        dist[x][y][t+1] = cost
                        heapq.heappush(pq, (cost, x, y, t+1))
        
        return min(dist[m-1][n-1])
