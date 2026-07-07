class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_pos = {}
        
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff_pos.get(diff) is None:
                diff_pos[nums[i]] = i
            else:
                return [diff_pos.get(diff),i]
        return []
        