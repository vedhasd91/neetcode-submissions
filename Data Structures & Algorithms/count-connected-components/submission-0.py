class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])


        visited = set()


        def dfs(node):
            if node in visited or node >=n:
                return

            visited.add(node)

            for nn in adj[node]:
                dfs(nn)


        comp = 0
        for i in range(n):
            if i not in visited:
                dfs(i)

                comp+=1
        
        return comp

        


        