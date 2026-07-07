class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        adj = {i:[] for i in range(0, numCourses)}

        for k,v in prerequisites:
            adj[k].append(v)

        order = []
        visited, cycle = set(), set()

        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True

            cycle.add(node)
            for crs in adj[node]:
                if not dfs(crs): return False
            cycle.remove(node)

            order.append(node)
            visited.add(node)
            return True



        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return order
        

        