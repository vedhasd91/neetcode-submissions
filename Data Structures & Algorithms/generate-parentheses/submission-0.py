class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        1 - ()
        2 - (()) () ()
        3 - ((())) ()()() (()())

        n open, n close

        can close if #open > #close
        """

        res , stack = [], []

        def backtrack(opcount, clcount):
            
            if opcount == clcount == n:
                res.append("".join(stack))
                return

            if opcount < n:
                stack.append('(')
                backtrack(opcount+1, clcount)
                stack.pop()

            if clcount < opcount:
                stack.append(')')
                backtrack(opcount, clcount+1)
                stack.pop()


        backtrack(0,0)

        return res


            
        