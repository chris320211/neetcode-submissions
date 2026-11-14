class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # arrays of intervals
        # intervals = [s, e]
        # return min num of inervals to remove
        # so no longer overlapping
        # unsorted so we have to sort by start times so we can iterate through
        #      4-6
        #    2-4
        # 1-----5
        # remove the one that ends later
        # greedy approach we just remove the one that ends later then
        # count up number of removals and that is best case
        # temp variable so we look at the prev one compare with current
        # overlap is when curr start is less than prev end

        intervals.sort(key=lambda i:i[0])
        result = 0
        prev = intervals[0]

        for i in range(len(intervals)):
            if i == 0:
                continue
            if intervals[i][0] < prev[1]:
                result += 1
                prev[1] = min(intervals[i][1], prev[1])
            else:
                prev = intervals[i]
        return result
                # we keep the one that ends early
                


