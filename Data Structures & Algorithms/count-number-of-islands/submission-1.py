class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def dfs(r, c):
            if r >= ROWS or r < 0 or c>= COLS or c<0 or grid[r][c] == "0":
                return

            if (r,c) in visited:
                return

            visited.add((r,c))

            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == "1":
                    dfs(row, col)
                    count+=1

        return count

        