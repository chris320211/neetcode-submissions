"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # array of meet time interval obj
        # find minimum numbers of room required ot schedule all the meetings, no conflicts
        # 0,8 8,10, end and start at same time, not a conflict

        # example 1
        # 0--------------------40
        #   5-10
        #        15-20
        # sort start
        # two pointer
        # start = [0 5 15], indicate meeting started at that time
        # end   = [10 20 40], indicates meeting has ended
        # 
        # if like two start and none end, two meeting same time, therefore 2 rooms
        # count for current rooms needed
        # max = global max count
        #
        # edge cases
        # start = 4
        # end = 9
        # [0, 10] [10, 15] [10, 40]
        # 0--10
        #    10-15
        #    10-----------40
        # start = [0 10 10]
        # end = [10 15 40]
        # 
        # end > start, compare next start, increase count by 1
        # end = start, compare next end 
        # end < start, compare next end, decrease count by 1

        start = []
        end = []

        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start.sort()
        end.sort()

        count = 0
        maxCount = 0
        s = 0
        e = 0

        while s < len(intervals):
            if end[e] > start[s]:
                count += 1
                s += 1
            elif end[e] == start[s]:
                e += 1
                count -= 1
            elif end[e] < start[s]:
                count -= 1
                e += 1
            maxCount = max(maxCount, count)
        
        return maxCount 
        
        # [1,5] [5,10] [10,15] [15,20]
        # 1
        # 1 5 10 15
        # 5 10 15 20
        
        


