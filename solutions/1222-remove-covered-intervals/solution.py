class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        c = 0
        mx = 0
        for s,e in intervals:
            if e > mx:
                c+=1
                mx = e
        return c
