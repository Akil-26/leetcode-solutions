class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        best = 0
        for i in range(n):
            ax1, ay1 = bottomLeft[i]
            ax2, ay2 = topRight[i]
            for j in range(i + 1, n):
                bx1, by1 = bottomLeft[j]
                bx2, by2 = topRight[j]
                # Compute overlap
                w = min(ax2, bx2) - max(ax1, bx1)
                if w <= 0:
                    continue
                h = min(ay2, by2) - max(ay1, by1)
                if h <= 0:
                    continue
                side = min(w, h)
                best = max(best, side * side)
        return best
