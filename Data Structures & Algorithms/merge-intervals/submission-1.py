class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # given array of intervals
        # interval = [start, end]
        # return array of non overlapping
        # sort by start times
        # 1--3
        #   2--5
        #        6-7
        # result array
        # overlap = next one starts before prev ones
        #         = 
        # merge = min of starts, max of ends

        intervals.sort(key=lambda i: i[0])
        result = []

        for i in range(len(intervals)):
            if i == 0:
                result.append(intervals[i])
                continue
            if intervals[i][0] <= result[-1][1]:
                newMin = min(intervals[i][0], result[-1][0])
                newMax = max(intervals[i][1], result[-1][1])
                result[-1] = [newMin, newMax]
            else:
                result.append(intervals[i])
        return result

        # intervals=[[1,2],[2,3]]
        # [[1,3]]
        # 1-2
        


            

        