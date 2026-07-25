class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def dfs(r, c):
            if r >= ROWS or r < 0 or c>= COLS or c<0 or grid[r][c] == "0":
                return False

            if (r,c) in visited:
                return False

            visited.add((r,c))

            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
            return True

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    if dfs(row, col):
                        count+=1

        return count

        