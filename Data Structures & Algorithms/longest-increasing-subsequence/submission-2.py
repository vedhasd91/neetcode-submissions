class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # min len starting at the end would be at least one
        # so one is the least LIS hence init cache with 1
        res = [1] * len(nums)

        """
        - - - - -
        """


        # start at the end of the seq and go back towards start
        for i in range(len(nums)-1, -1, -1):
            # at each index we will compare the LIS till the end of list
            for j in range(i+1, len(nums)):
                # compare if the two nums are in increasing order
                if nums[i] < nums[j]:
                    # len of LIS at the current index
                    res[i] = max(res[i], 1 + res[j])

        return max(res)
        