class Solution:
    def rob(self, nums: List[int]) -> int:

        """    i+2
        3 --- 3 --- 
          +
          --- 0 --- 4
        4 --- ##
          +
        
        3

        0 4 _

        dp[i] = max(nums[i] + dp[i-2] , dp[i-1])
        """

        n = len(nums)

        if n == 1:
            return nums[0]

        memo = [[-1]*2 for _ in range(n)]

        def dfs(i, start):
            if i >= n or (i == n-1 and start == 0):
                return 0

            if memo[i][start] != -1:
                return memo[i][start]
            else:
                memo[i][start] = max(dfs(i+1, start), nums[i] + dfs(i+2, start))
                return memo[i][start]

        return max(dfs(0,0), dfs(1,1))            
        