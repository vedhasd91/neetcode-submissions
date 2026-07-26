class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    fresh +=1
        
        t = 0
        # we put fresh > 0 since the q has rotten to start with
        # so the last rotten will be there even if no fresh orange is available 
        # and it will increment the time
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    rr, cc = r+dr, c+dc
                    if rr < ROWS and rr >=0 and cc < COLS and cc >= 0 and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        q.append((rr, cc))
                        fresh -= 1
            t+=1

        return t if fresh == 0 else -1
        