class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        n = 26
        
        # distance matrix
        dist = [[INF]*n for _ in range(n)]
        
        # cost to stay same = 0
        for i in range(n):
            dist[i][i] = 0
        
        # direct conversions
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # compute total cost
        ans = 0
        for s, t in zip(source, target):
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            ans += dist[u][v]
        
        return ans
