# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def dfs(node, k):
            if not node:
                return node

            if k < node.val:
                node.left = dfs(node.left, k)
            elif k > node.val:
                node.right = dfs(node.right, k)
            else:
                # we found the value to yank

                # if one of the children is None then simply return the other
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                # Both children are present, remove the correct one -- min from right subtree
                # cur = node.right
                # while cur.left:
                #     cur = cur.left
                
                # node.val = cur.val
                # node.right = dfs(node.right, cur.val)

                # Both children are present, remove the correct one -- max from left subtree
                cur = node.left
                while cur.right:
                    cur = cur.right
                
                node.val = cur.val
                node.left = dfs(node.left, cur.val)

            return node

        return dfs(root, key)
            



        


        