class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        area = 0

        def bfs(r,c):
            ar = 1
            visited.add((r,c))
            frontier = [(r,c)]

            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            while frontier:
                row ,col = frontier.pop(0)
                

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if ((0 <= nr < rows) and (0 <= nc < cols) and 
                    grid[nr][nc] == 1 and ((nr,nc) not in visited)):

                        
                        visited.add((nr,nc))
                        frontier.append((nr,nc))
                        ar +=1

            return ar


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: 
                    area = max(bfs(i, j), area)
        
        return area