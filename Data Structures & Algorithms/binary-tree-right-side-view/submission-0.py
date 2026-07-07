# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        """

        """
        res = []
        
        if root is None:
            return res

        dq = deque()
        dq.append(root)

        while(dq):
            q_len = len(dq)

            for i in range(0, q_len):
                node = dq.popleft()

                if i == q_len-1:
                    res.append(node.val)
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return res
        