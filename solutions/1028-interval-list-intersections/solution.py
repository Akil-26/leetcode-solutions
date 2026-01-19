class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(fl) and j < len(sl):
            s = max(fl[i][0],sl[j][0])
            e = min(fl[i][1],sl[j][1])

            if s <= e:
                ans.append([s,e])
            
            if fl[i][1] == sl[j][1]:
                i+=1
                j+=1
            elif fl[i][1] < sl[j][1]:
                i+=1
            else:
                j+=1
        return ans
