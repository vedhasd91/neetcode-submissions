class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search_idx(nums, l, h, target):
            
            if l > h:
                return -1

            center = (l+h)//2

            print(center,l,h, nums)
            
            if nums[center] == target:
                return center
            elif target > nums[center]:
                return search_idx(nums, center+1, h, target)
            elif target < nums[center]:
                return search_idx(nums, l,center-1, target)

        return search_idx(nums,0,len(nums)-1,target)    