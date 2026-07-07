class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # one way to avoid duplicate is to sort -- this arranges duplicates near by
        # skip them by moving the pointer
        nums.sort()
        out = []


        for i, a in enumerate(nums):

            if i > 0 and nums[i-1] == a:
                continue
            

            #recalibrate pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sm = a + nums[l] + nums[r]
                if 0 == sm:
                    out.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif sm < 0:
                    l+=1
                elif sm > 0:
                    r-=1

        return out

            


        