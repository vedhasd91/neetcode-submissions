# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
    
        dq = deque([root]) if root else deque()
        res = []

        while dq:

            q_len = len(dq)

            level = []
            for i in range(q_len):
                node = dq.popleft()

                level.append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if level:
                res.append(level)

        
        return res


        