class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1, max(piles)
        n = len(piles)
        res = r

        while l <= r:

            k = (l+r)//2

            h_c = 0
            for i in range(n):
                h_c += math.ceil(piles[i]/k)
                if h_c > h:
                    break

            if h_c <= h:
                res = min(res, k)
                r=k-1
            else:
                l=k+1

        return res