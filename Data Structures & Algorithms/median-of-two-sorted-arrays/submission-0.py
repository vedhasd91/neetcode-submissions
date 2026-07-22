class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # nums1: _  _|   _   _   _
        #           Bl  Br
        # nums2: _  _|   _
        #           Al  Ar


        A = nums1
        B = nums2

        if len(nums1) > len(nums2):
            A, B = nums2, nums1

        l = 0
        r = len(A) - 1

        total = len(A) + len(B)
        mid = total//2

        while True:
            # Pointers to numbers near partition boundary
            i = (l + r)// 2
            j = mid - i - 2

            Aleft = A[i] if i >= 0 else -math.inf
            Aright = A[i+1] if i + 1 < len(A) else math.inf

            Bleft = B[j] if j >= 0 else -math.inf
            Bright = B[j+1] if j +1 < len(B) else math.inf

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

