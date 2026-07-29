"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        cloned = {}

        def dfs(node):
            if not node:
                return None

            if node in cloned:
                return cloned[node]

            new_node = Node()
            new_node.val = node.val

            cloned[node] = new_node

            for n in node.neighbors:
                if nta:=dfs(n):
                    new_node.neighbors.append(nta)

            return new_node


        return dfs(node)