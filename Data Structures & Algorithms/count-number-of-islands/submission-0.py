class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col = len(grid)
        row = len(grid[0])
        isl = 0

        def dfs(i,j,grid):
            if i < 0 or i >= col:
                return
            
            if j < 0 or j>= row:
                return

            if grid[i][j] == "0":
                return

            if grid[i][j] == "1":
                grid[i][j] = "0"

            dfs(i+1,j,grid)
            dfs(i-1,j,grid)
            dfs(i,j+1,grid)
            dfs(i,j-1,grid)

        for i in range(col):
            for j in range(row):
                if grid[i][j] == "1":
                    dfs(i,j,grid)
                    isl += 1
        
        return isl
        