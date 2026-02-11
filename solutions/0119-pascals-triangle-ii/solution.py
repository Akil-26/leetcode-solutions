class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = []
        for i in range(1,rowIndex+2):
            row = [0]*i
            row[0] = 1
            row[-1] = 1
            if len(row) > 2 :
                for j in range(1,len(row)-1):
                    row[j] = tri[-1][j-1] + tri[-1][j]
            tri.append(row)
        return tri[rowIndex]
