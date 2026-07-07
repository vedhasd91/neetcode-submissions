class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        nums.sort()

        a = 0
        l = a + 1
        r = len(nums) - 1

        out = []
        first = set()

        for a in range(len(nums)):
        
            if nums[a] in first:
                continue
            else:
                first.add(nums[a])
                l = a + 1
                r = len(nums) - 1
                lset = set()
                rset = set()
                while l < r:
                    tsum = nums[a] + nums[l] + nums[r]
                    if tsum == 0:
                        out.append([nums[a], nums[l], nums[r]])
                        lset.add(nums[l])
                        rset.add(nums[r])
                        while nums[l] in lset and l < r:
                            l += 1
                        while nums[r] in rset and l < r:
                            r -= 1
                    elif tsum < 0:
                        l += 1
                    elif tsum > 0:
                        r -= 1

        return out