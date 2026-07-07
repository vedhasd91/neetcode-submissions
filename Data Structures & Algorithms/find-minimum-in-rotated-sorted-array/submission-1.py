class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 1001

        l = 0
        r = len(nums) - 1
        

        while l <= r:
            # if not rotated
            if(nums[l] < nums[r]):
                res = min(res,nums[l])
                return res
            

            m = (l + r) // 2

            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1

        return res
