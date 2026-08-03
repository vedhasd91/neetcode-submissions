class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visit = set()

        def dfs(root, parent):
            if root in visit:
                return False

            visit.add(root)

            for node in adj[root]:
                if node == parent:
                    continue
                if not dfs(node, root): return False

            return True

        return len(visit) == n if dfs(0, -1) else False
        
        