class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(1,numRows+1):
            row = [0] * i
            row[0] = 1
            row[-1] = 1
            if len(row) > 2:
                for j in range(1, len(row) - 1):
                    row[j] = tri[-1][j - 1] + tri[-1][j]
            tri.append(row)
        return tri
