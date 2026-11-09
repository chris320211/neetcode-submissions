class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # given an array of intervals where intervals[i] start and end
        # merge all overlapping
        # return array of non overlapping intervals that cover the range
        # sort, unsorted
        # sort by start
        # 1 3
        #  2  4
        #   5 7
        intervals.sort(key = lambda i:i[0])
        result = []

        for i in range(len(intervals)):
            if i == 0:
                result.append(intervals[0])
                continue
            recent = result[-1]
            if intervals[i][0] > recent[1]:
                result.append(intervals[i])
            elif intervals[i][0] <= recent[1]:
                start = min(intervals[i][0], recent[0])
                end = max(intervals[i][1], recent[1]) 
                result[-1] = [start, end]
        return result

        