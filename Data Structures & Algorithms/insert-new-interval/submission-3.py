class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # given an array of non overlapping interval
        # insert interval, no overlaps
        # array is sorted, return sorted
        # [1, 2] [2, 3] considered overlapping
        # newIntervla comapred with prev interval
        # [0, 1]
        # [2,5]
        # merge, min of start, max of end
        # [1, 5]
        # [4, 6]
        # result array
        
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[0] <= intervals[i][1]:
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end]
        res.append(newInterval)

        return res

                

        


    
