class Solution:
    def largestSubmatrix(self, grid):
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and r > 0:
                    grid[r][c] += grid[r - 1][c]
            heights = sorted(grid[r])
            for i in range(cols - 1, -1, -1):
                width = cols - i
                area = heights[i] * width
                max_area = max(max_area, area)
        return max_area
