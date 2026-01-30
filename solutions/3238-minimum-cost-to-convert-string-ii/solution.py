class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        m = len(original)
        INF = 10**18

        # Map each string to id
        all_strings = list(set(original + changed))
        idx = {s:i for i,s in enumerate(all_strings)}
        k = len(all_strings)

        # Floyd Warshall graph
        dist = [[INF]*k for _ in range(k)]
        for i in range(k):
            dist[i][i] = 0

        for i in range(m):
            u = idx[original[i]]
            v = idx[changed[i]]
            dist[u][v] = min(dist[u][v], cost[i])

        # APSP
        for x in range(k):
            for i in range(k):
                for j in range(k):
                    if dist[i][x] + dist[x][j] < dist[i][j]:
                        dist[i][j] = dist[i][x] + dist[x][j]

        # Pre-group rules by length
        rules = {}
        for s in all_strings:
            rules.setdefault(len(s), []).append(s)

        # DP
        dp = [INF]*(n+1)
        dp[n] = 0

        for i in range(n-1, -1, -1):
            # char skip
            if source[i] == target[i]:
                dp[i] = dp[i+1]

            # try every possible substring length
            for L in rules:
                if i+L > n:
                    continue
                a = source[i:i+L]
                b = target[i:i+L]
                if a in idx and b in idx:
                    u = idx[a]
                    v = idx[b]
                    if dist[u][v] < INF:
                        dp[i] = min(dp[i], dist[u][v] + dp[i+L])

        return -1 if dp[0] == INF else dp[0]

