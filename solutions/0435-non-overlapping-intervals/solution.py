class Solution:
    def eraseOverlapIntervals(self, i: List[List[int]]) -> int:
        i.sort(key=lambda x:x[1])
        rm = 0
        pre_end = i[0][1]
        for j in range(1,len(i)):
            if i[j][0] < pre_end:
                rm += 1
            else:
                pre_end = i[j][1]
        return rm
