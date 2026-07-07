import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._nums = nums

        heapq.heapify(self._nums)

        while len(self._nums) > self._k:
            heapq.heappop(self._nums)
            
    # def heapify(self,nums):
    #     start = len(nums)//2 - 1
    #     for i in range(start, -1, -1):
    #         self.min_heapify(nums, i)

    # def min_heapify(self, nums, pos):
        
    #     smallest = pos
    #     left = 2*pos+1
    #     right = 2*pos+2

    #     if left < len(nums) and nums[left] < nums[smallest]:
    #         smallest = left

    #     if right < len(nums) and nums[right] < nums[smallest]:
    #         smallest = right

    #     if smallest != pos:
    #         nums[smallest], nums[pos] = nums[pos], nums[smallest]

    #         self.min_heapify(nums, smallest)

    def add(self, val: int) -> int:
        heapq.heappush(self._nums,val)
        
        while len(self._nums) > self._k:
            heapq.heappop(self._nums)
        
        print(self._nums)
        return self._nums[0]
        
