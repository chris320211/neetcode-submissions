class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # array fo intervals
        # return min num of intervals we need to remove so no overlaps
        # sort by start
        # [1,2], [1,4], [2,4]
        intervals.sort(key=lambda i:i[0])

        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                res += 1
                prevEnd = min(intervals[i][1], prevEnd)
        return res