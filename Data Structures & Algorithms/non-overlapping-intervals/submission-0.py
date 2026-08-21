class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])

        pre_end = intervals[0][1]

        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < pre_end:
                pre_end = min(pre_end, intervals[i][1])
                res+=1
            else:
                pre_end = intervals[i][1]

        return res
        