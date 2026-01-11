class Solution:
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        h, ans = [0]*len(matrix[0]), 0

        for r in matrix:
            for i, v in enumerate(r):
                h[i] = h[i] + 1 if v == '1' else 0

            st = []
            for i in range(len(h)+1):
                cur = h[i] if i < len(h) else 0
                while st and cur < h[st[-1]]:
                    height = h[st.pop()]
                    width = i if not st else i - st[-1] - 1
                    ans = max(ans, height * width)
                st.append(i)
        return ans

