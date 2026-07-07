class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        l = 0
        r = n-1

        lc = height[l]
        rc = height[r]

        water = 0
        while l<r:
            if lc < rc:
                l+=1
                lc = max(lc, height[l])
                water += lc - height[l]
            else:
                r -=1
                rc = max(rc, height[r])
                water += rc - height[r]

            print(l, r, water, lc, rc)
        
        return water


        