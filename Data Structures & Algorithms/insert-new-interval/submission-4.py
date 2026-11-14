class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # array on non overlap intervals, sorted by start
        # interval = array with [s, e]
        # given new interval to insert
        # loop through intervals
        # if overlapping or not
        # [1, 3]
        # [2, 4]
        # newInterval start <= currInterval end (overlap)
        # if it is we merge
        # min of start val, max of end val
        # result
        # [1, 3] [4-5] [6-7] [8-10]
        #   [100-102]
        # we update the newInterval variable as we merge
        # we check when the one we r looking at starts after
        # [[1,3], ]

        result = []

        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newMin = min(intervals[i][0], newInterval[0])
                newMax = max(intervals[i][1], newInterval[1])
                newInterval = [newMin, newMax]
        
        result.append(newInterval)
        return result



                

        


    
