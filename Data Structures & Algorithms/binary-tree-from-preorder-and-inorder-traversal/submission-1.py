# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        """
        preorder =  | 1 | 2 | 3 | 4 |
                    ---- +++
                        |mid|

                        _mid_
        inorder =   | 2 | 1 | 3 | 4 |

        """
        # root = TreeNode(val=preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # return root
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_id = 0
        def dfs(l, r):
            if l > r:
                return None

            rv = preorder[self.pre_id]
            self.pre_id += 1
            root = TreeNode(rv)
            mid = indices[rv]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root

        return dfs(0, len(inorder)-1)