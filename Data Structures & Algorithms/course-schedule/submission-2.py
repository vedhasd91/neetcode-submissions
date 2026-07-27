class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for crs, dep in prerequisites:
            adj[crs].append(dep)

        visited = set()
        def dfs(i):
            if i in visited:
                return False

            if adj[i] == []:
                return True


            visited.add(i)

            for crs in adj[i]:
                if not dfs(crs): return False

            # this means crs can be done w/o cycle
            visited.remove(i)
            adj[i] = []

            return True
            


        for i in range(numCourses):
            if not dfs(i): return False
        return True

        