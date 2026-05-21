class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(st,target,summ):
            if 0 == target:
                res.append(list(summ))
                return
            for i in range(st,len(candidates)):
                if i > st and candidates[i] == candidates[i-1]:
                    continue 
                if candidates[i] > target:
                    break
                summ.append(candidates[i])
                dfs(i+1,target - candidates[i],summ)
                summ.pop()
        dfs(0,target,[])
        return res
