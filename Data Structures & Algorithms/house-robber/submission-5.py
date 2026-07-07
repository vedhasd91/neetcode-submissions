class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        
        nums[i] --> money ith house

        i-1, i, i+1


        [ 1| 1| 3| 3| 5| 7]__

        [ 1| 1| 4| 4| 9| 11]__|.   nums[i] + dp[i-2], dp[i-1]
        

        """
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        n = len(nums)

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            print(nums)
            print(dp)

        return dp[-1]
    
        
        