class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        if not heights:
            return res
        
        l, r = 0, len(heights)-1

        while l<r:

            ht = min(heights[l], heights[r])
            lt = r-l

            res = max(res, ht*lt)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1


        return res

            