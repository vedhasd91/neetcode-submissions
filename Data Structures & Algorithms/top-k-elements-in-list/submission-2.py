class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num]+=1

        topk = [(f,n) for n, f in count.items()]

        heapq.heapify(topk)

        while len(topk) != k:
            heapq.heappop(topk)

        return [n for _, n in topk] 
            
        