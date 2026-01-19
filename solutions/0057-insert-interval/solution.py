class Solution:
    def insert(self, i: List[List[int]], newi: List[int]) -> List[List[int]]:
        i.append(newi)
        i.sort(key=lambda x:x[0])
        ans = []
        for item in i:
            if not ans or ans[-1][1] < item[0]:
                ans.append(item)
            else:
                ans[-1][1] = max(ans[-1][1],item[1])
        return ans
