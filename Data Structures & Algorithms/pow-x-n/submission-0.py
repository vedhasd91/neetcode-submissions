class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        x^2 = x*x
        x^-2 = 1/x*x


        _ _ _

        """

        def pow(n):
            if n == 0:
                return 1
            if x == 0:
                return 0

            res = pow(n//2)
            res = res * res
            
            return res*x  if n%2 else res
             

        if n>=0: 
            return pow(n)
        else:
            return 1/pow(abs(n))