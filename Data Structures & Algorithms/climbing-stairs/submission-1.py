class Solution:
    def climbStairs(self, n: int) -> int:

        """"
        n -- # steps to top of stairs
        1, 2


        n=1 --> total way 1
        1

        n=2 --> total ways 2
        1+1
        2

        3
        1+1+1
        2+1
        1+2
        """
        if n <= 2:
            return n

        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]



        return dp[n]

