class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 1001

        l = 0
        r = len(nums)-1

        while l<=r:
            if nums[l] <= nums[r]:
                res = min(res,nums[l])
                break

            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] <= nums[r]:
                # right is sorted so min is in left part including m
                r = m-1
            else:
                l = m+1

        return res

            

            



        