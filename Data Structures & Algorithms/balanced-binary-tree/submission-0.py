# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if root is None:
                return True, 0

            l_bal, left = dfs(root.left)
            r_bal, right = dfs(root.right)

            diff = abs(left-right)

            return (l_bal and r_bal and diff <= 1), 1 + max(left, right)

        bal, ht = dfs(root)

        return bal