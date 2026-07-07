class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        area = 0

        """
        height=[1,7,2,5,4,7,3,6]
                    |       |

        """
        while l < r:
            lc = heights[l]

            rc = heights[r]

            area = max(area, min(lc,rc) * (r - l))

            print(area, lc, rc, r-l)
            
            if lc <= rc:
                l += 1
            else:
                r -= 1
        
        return area

        