class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # array of intervals
        # intervals = [start, end]
        # return the min num of intervasl we need to remove so no overlaps
        # sort by start so we can look at it in order
        # 1-2
        #.   2--4
        # 1-----4
        # here we see 1-2 and 1--4 overlap
        # we keep the one htat ends sooner since the 1--4 takes up more room
        # more chance to overlap with alter intervals and here it does
        # greedy approach we remove what we have to remove when we loop through
        # we know overlap if one we are looking at and prev one
        # if curr start < prev end
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda i:i[0])
        res = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                prev[1] = min(intervals[i][1], prev[1])
                res += 1
            else:
                prev = intervals[i]
        return res

        # intervals=[[1,2],[2,4],[1,4]]
        # 1-2
        #.   2-4
        # 1----4
        # prev = [1,2]
        # intervals[i] = 