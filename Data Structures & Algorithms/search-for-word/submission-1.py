class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        visit = set()

        res = []

        def dfs(r, c, concat, word):

            if (r<0 or c<0 or r==ROWS or c==COLS or ((r,c) in visit)):
                return
            
            visit.add((r,c))
            concat+=board[r][c]
            if concat == word:
                res.append(concat)
                return
            

            dfs(r+1,c, concat, word)
            dfs(r-1,c, concat, word)
            dfs(r,c+1, concat, word)
            dfs(r,c-1, concat, word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", word)

        return len(res)>=1
            
        