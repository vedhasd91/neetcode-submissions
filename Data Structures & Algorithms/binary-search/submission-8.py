class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(l, r, arr, target):
            l = l
            r = r

            if l > r:
                return -1

            m = (l + r) // 2


            if arr[m] == target:
                return m
            elif target < arr[m]:
                return binary_search(l, m-1, arr, target)
            elif target > arr[m]:
                return binary_search(m+1, r, arr, target)

        l = 0
        r = len(nums) - 1

        return binary_search(l, r, nums, target)

            
        