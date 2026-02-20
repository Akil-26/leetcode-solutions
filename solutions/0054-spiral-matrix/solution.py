class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t,d = 0,len(matrix)-1
        l,r = 0,len(matrix[0])-1
        res = []
        while t <= d and l <= r:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            for j in range(t,d+1):
                res.append(matrix[j][r])
            r-=1
            if t<=d:
                for i in range(r,l-1,-1):
                    res.append(matrix[d][i])
                d-=1
            if l<=r:
                for j in range(d,t-1,-1):
                    res.append(matrix[j][l])
                l+=1
        return res
