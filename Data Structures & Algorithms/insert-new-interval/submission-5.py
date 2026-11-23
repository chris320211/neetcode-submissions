class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # array of non overlapping intervals, sorted intially by start
        # interval = [start, end]
        # newInterval
        # we want to insert it so its still sorted and non overlapping
        # loop through intervasl from left
        # find where it goes, if overlap we merge
        # if not we just add

        # 1--3
        #    3--6
        #.     
        #.         10-12
        # comparing against prev
        # overlap since new start less than prev end
        # min of starts, max of the ends for the merged
        # we are done when we find the case where it overlaps witha next interval
        # we merge then we are done

        # result list
        # if this current oen doesnt overlap we just add
        # new start less than prev end
        # new end is greater than next start
        # new interval as merged one continue comparing with each

        result = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newStart = min(intervals[i][0], newInterval[0])
                newEnd = max(intervals[i][1], newInterval[1])
                newInterval = [newStart, newEnd]
        result.append(newInterval)
        return result


