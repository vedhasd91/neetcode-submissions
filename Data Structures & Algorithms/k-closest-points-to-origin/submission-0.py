class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dorg(x, y):
            return math.sqrt(x**2 + y**2), x, y

        if not points:
            return [[]]

        if not points[0]:
            return [[]]

        #dist from orig
        orig = []
        for i in range(len(points)):
            x, y = points[i]
            orig.append(dorg(x, y))


        heapq.heapify(orig)

        res = []
        while k:
            _, x, y = heapq.heappop(orig)

            res.append([x,y])

            k-=1

        return res
        