class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # instead of running dfs from every cell, we can run dfs from the rows touchging the ocean
        # simulating water entering from the ocean

        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visit, prev_ht):
            if ((r,c) in visit or r == ROWS or c == COLS
                or r < 0 or c < 0 or heights[r][c] < prev_ht):
                return

            visit.add((r, c))

            for dr, dc in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r+dr, c+dc, visit, heights[r][c])
        
        # run from top and bottom row
        # for each col in top and bottom row
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        # run from left and right col
        # for each col in top and bottom row
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl,heights[r][COLS-1])

        return list(pac & atl)