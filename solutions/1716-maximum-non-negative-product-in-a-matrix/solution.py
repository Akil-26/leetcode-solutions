class Solution:
    def maxProductPath(self, g: List[List[int]]) -> int:
        m,n =len(g),len(g[0])
        f = cache(lambda i,j:(i,j)==(m-1,n-1) and [g[i][j]] or m>i>=0<=j<n and \
            [*itemgetter(0,-1)(sorted(g[i][j]*q for q in f(i+1,j)+f(i,j+1)))] or [])
        
        return (f(0,0)[-1]%(10**9+7),-1)[f(0,0)[-1]<0]
