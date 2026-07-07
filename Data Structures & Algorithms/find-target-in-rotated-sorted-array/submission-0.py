class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        1 2 3 4 5
        l < m < r --> fully rotated or not rotated


        4 5 1 2 3
        l > m < r --> left sorted, right sorted

        3 4 5 1 2 
        l < m > r --> left sorted, right sorted

        """

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l+r)//2

            if target == nums[m]:
                return m

            # the outer conditions determine the case of where is the array pivoted
            if nums[l] <= nums[m]:
                # check target is in rotated part or not
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m -1


        return -1


            
        