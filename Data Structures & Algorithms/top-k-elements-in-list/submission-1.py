class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda:0)

        for num in nums:
            count[num]+=1

        items = sorted(count.items(),key=lambda t: t[1])

        return [item[0] for item in items][-k:] 
            
        