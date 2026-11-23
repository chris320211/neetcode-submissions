class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # given an array of intervals
        # interval is [start, end]
        # merge all overlapping intervals
        # how do we know they overlap
        # prev vs curr
        # curr start is less than prev end
        # overlap, we take the min of start, and max of ends to merge

        # res array, the top is the prev interval
        # if they overlap, we merge and update the top with it
        # as we iterate we compare with the curr witht he prev which is the top

        intervals.sort(key=lambda i:i[0])
        res = []

        for i in range(len(intervals)):
            if len(res) == 0:
                res.append(intervals[i])
                continue
            if intervals[i][0] <= res[-1][1]:
                newStart = min(intervals[i][0], res[-1][0])
                newEnd = max(intervals[i][1], res[-1][1])
                res[-1] = [newStart, newEnd]
            else:
                res.append(intervals[i])
        
        return res