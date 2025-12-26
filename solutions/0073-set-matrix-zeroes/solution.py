class Solution:
    def setZeroes(self, matrix):
        rows ,cols = [] ,[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for k in range(len(rows)):
            row = rows[k]
            col = cols[k]
            for i in range(len(matrix)):
                matrix[i][col] = 0
            matrix[row] = [0] * len(matrix[0])
