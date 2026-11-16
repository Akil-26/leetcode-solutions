class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        vis = set()
        for i in edges:
            if i[0] in vis:
                res = i[0]
            if i[1] in vis:
                res = i[1]
            vis.add(i[0])
            vis.add(i[1])
        return res