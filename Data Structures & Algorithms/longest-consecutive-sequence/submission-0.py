class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nst = set(nums)

        res = 0

        for n in nst:
            count = 0
            if n-1 not in nst:
                count += 1

                j = n+1
                while j in nst:
                    count += 1
                    j += 1
            
            print(res, count)
            res = max(res,count)
                

        return res

        