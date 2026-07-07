class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
             
            [30,38,30,36,35,40,28]

            [1,4,1,2,1,0,0]

        """
        n = len(temperatures)
        stack = []
        res = [0] * n


        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idn = stack[-1]
                res[idn]=i-idn
                stack.pop()

            stack.append(i)
            

        return res

        

