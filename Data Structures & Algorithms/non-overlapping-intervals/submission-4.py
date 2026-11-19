class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # array of intervals
        # interval = [start, end]
        # return the min num of intervals need to remove to ensure no overlaps
        
        # sort, so we look at it in order, sequentially, no need to rescan
        # 1-2
        #.  2--4
        # 1----4
        # we remove 1-4, we want to keep the one that ends earlier so it takes up less
        # how do we know overlap, we compare 1-2 and 1-4 first since sort by start
        # overlap since one starts before the other one ends
        # we remove the one that ends later
        # 
        # loop through intervals after sort
        # keep track of the prev
        # 1-2 compared to 1-4
        # prev = 1-2
        # overlap so we update prev to 1-2 to keep shorter one
        # incremenet remove to 1
        # then compare to next one whcih is 2-4
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda i:i[0])

        result = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                if intervals[i][1] < prev[1]:
                    prev = intervals[i]
                    result += 1
                else:
                    result += 1
            else:
                prev = intervals[i]
        
        return result
                    