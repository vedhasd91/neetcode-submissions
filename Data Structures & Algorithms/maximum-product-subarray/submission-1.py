class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curmax, curmin = 1, 1

        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            
            savd_curmax = n*curmax
            curmax = max(n*curmax, n*curmin, n)
            curmin = min(savd_curmax, n*curmin, n)

            res = max(res, curmax)

        return res

