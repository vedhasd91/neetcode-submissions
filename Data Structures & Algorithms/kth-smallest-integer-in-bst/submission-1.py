# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        n = 0
        res = root.val

        def dfs(root):
            nonlocal n, res

            if not root:
                return

            dfs(root.left)
            if n==k:
                return

            n+=1
            if n==k:
                res = root.val
                return

            dfs(root.right)

        dfs(root)

        return res