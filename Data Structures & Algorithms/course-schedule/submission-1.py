class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for i in range(len(prerequisites)):
            crs, dep = prerequisites[i]
            adj[crs].append(dep)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if adj[crs] == []:
                return True

            
            visited.add(crs)
            for i in adj[crs]:
                if not dfs(i): 
                    return False

            # reson we remove is because we are done exploring 
            # the nodes without cycle via this path. There could be other 
            # inward path on this node which is disconneted to this path
            # so we want to be able to visit this
            visited.remove(crs) 

            # this marks that this course can be done w/o cycle.
            adj[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True



        


