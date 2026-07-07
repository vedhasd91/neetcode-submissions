class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1

        area = 0

        while l < r:
            
            print(l, r)
            lc = heights[l]
            rc = heights[r]

            area = max(area, min(lc, rc) * (r - l))

            if lc <= rc:
                l += 1
            else:
                r -= 1

        return area
        