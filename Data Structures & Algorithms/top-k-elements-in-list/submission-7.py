class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        heap = [(-f, n) for n, f in freq.items()]

        heapq.heapify(heap)

        res = []
        while k:
            f, n = heapq.heappop(heap)
            res.append(n)
            k-=1
        return res

        