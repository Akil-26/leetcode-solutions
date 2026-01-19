class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:
        i.sort(key=lambda x:x[0])
        merged = []
        for s,e in i:
            if not merged:
                merged.append([s,e])
            elif s <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],e)
            else:
                merged.append([s,e])
        return merged
