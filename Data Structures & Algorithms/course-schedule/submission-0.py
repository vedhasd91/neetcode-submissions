class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        path = {i:[] for i in range(0, numCourses)}
        
        for crses in prerequisites:
            k, v = crses
            path[k].append(v)


        visited = set()

        
        def dfs(i):
            
            if i in visited:
                # detected cycle
                return False
            if path[i] == []:
                # completable course
                return True

            visited.add(i)
            for crs in path[i]:
                if not dfs(crs): return False

            path[i] = [] # course can be completed independently
            visited.remove(i)

            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return False    



        
        return True
        