class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1,2,3,4,5,6

        6,1,2,3,4,5 -- 1

        5,6,1,2,3,4 -- 2

        4,5,6,1,2,3, -- 3

        3, 4, 5, 6, 1, 2 -- 4
        """

        l, r = 0, len(nums)-1

        while l <= r:

            m = (l+r)//2

            if nums[m] == target:
                return m
            
            # left sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r = m-1
            # right sorted
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1
        