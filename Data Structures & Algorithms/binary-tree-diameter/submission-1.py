# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def calculate_height(root):
            nonlocal res
            
            if root is None:
                return 0

            left = calculate_height(root.left)
            right = calculate_height(root.right)

            res = max(res, left + right)

            return 1 + max(left, right)
            
        calculate_height(root)

        return res