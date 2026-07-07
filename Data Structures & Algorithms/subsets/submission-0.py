class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Tried building intuition but had to go through greg
        hogg's solution which is clean in understanding.
        
        The intuition is to navigate to the end of the tree ... leaf node.
        At each level there will be two branches pick or not pick i.e
        solution or not a solution. The actual answer to the solution
        would only be at the leaf nodes but in order to go to other
        leaf nodes we need to backtrack and hence pop an item ... intermediate sol
        """

        n = len(nums)

        res, sol = [], []

        def backtrack(pos):
            
            if pos == n:
                res.append(sol[:])
                return

            # do not pick
            backtrack(pos+1)

            # pick
            sol.append(nums[pos])
            backtrack(pos+1)
            sol.pop()

        backtrack(0)

        return res