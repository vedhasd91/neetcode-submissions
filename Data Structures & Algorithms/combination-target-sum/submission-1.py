class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        res, sol = [], []

        def backtrack(pos):

            """Base case where a combination is equal to the target"""
            if sum(sol) == target:
                res.append(sol[:])
                return
            
            """return if going out of bounds"""
            if pos == n or sum(sol) > target:
                return

            """Choice: do not choose the element branch"""
            backtrack(pos+1)

            """Add the element to solution and consider 
            all options till the target is reach with using the same
            value at index plus others"""
            sol.append(nums[pos])
            backtrack(pos)
            sol.pop()

            
        backtrack(0)
        return res
        