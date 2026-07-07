# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(a, b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)
            
            return False

        if not subRoot:
            return True
        if not root:
            return False

        if is_same_tree(root, subRoot):
            return True

        is_left = self.isSubtree(root.left, subRoot)
        is_right = self.isSubtree(root.right, subRoot)
        
        return is_left or is_right