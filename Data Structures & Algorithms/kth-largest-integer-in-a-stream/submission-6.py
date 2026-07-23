class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._nums = nums
        heapq.heapify(self._nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self._nums, val)
        while len(self._nums) > self._k:
            heapq.heappop(self._nums)

        return self._nums[0]

        
        
