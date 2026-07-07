class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        """

        if start from 0:

        cost[0] --> cost of going from here

        dp[0] --> cost to be here --> 0

        cost[1] --> cost of going from here

        dp[1] --> cost to be here --> 0



        """
        if not cost:
            return 0

        if len(cost) <= 2:
            return min(cost)

        n = len(cost)
        dp = [0] * (n + 1)
        

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

            print(cost)
            print(dp)
            


        return dp[i]

        