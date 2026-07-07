class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        sol = []

        def dfs(pos, sol):
            if sum(sol) == target:
                res.append(sol[:])
                return
            if pos >= len(candidates) or sum(sol) > target:
                return

            # skip pos and pos duplicates
            ori_pos = pos
            while pos + 1 < len(candidates) and candidates[pos] == candidates[pos+1]:
                pos+=1
            dfs(pos+1, sol)
            

            # include pos and pos duplicates
            sol.append(candidates[pos])
            dfs(ori_pos+1, sol)
            sol.pop()

        dfs(0, sol)
        return res
        