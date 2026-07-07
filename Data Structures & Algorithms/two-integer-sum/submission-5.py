class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff = {}
        res = []

        for i in range(len(nums)):
            delta = target - nums[i]
            if nums[i] in diff:
                return [diff[nums[i]], i]
            else:
                diff[delta] = i
        
        return res