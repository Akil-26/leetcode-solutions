class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,cur):
            if sum(cur) == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or sum(cur) > target:
                return
            cur.append(candidates[i])
            dfs(i,cur)
            cur.pop()
            dfs(i+1,cur)
            return
        dfs(0,[])
        return res