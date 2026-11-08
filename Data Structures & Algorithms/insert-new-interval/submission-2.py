class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #2d array intervals
        # inside are intervals, ascneding order
        # want to add the new interval to intervals
        # without overlapping
        # ex: 1-3
        # add: 2-5
        # new is 1-5, take min and max since they overlap
        # return intervals non overlapping and ascneding by start
        # 1-2
        # 2-3 is also overlapping since 2 occurs twice so combined to 1-3
        # check if overlapping, if they are we merge

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                start = min(intervals[i][0], newInterval[0])
                end = max(intervals[i][1], newInterval[1])
                newInterval = [start, end]
        res.append(newInterval)
        return res

        

        


    
