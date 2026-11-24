"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start and end arrays
        # both sorted
        # we keep count of start
        # we subtract count when end times occur
        # we go by times
        # intervals = [(0,40),(5,10),(15,20)]
        # start = 0 10 15
        # end = 10 20 40
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        
        start.sort()
        end.sort()
        res = 0
        curr = 0
        s = 0
        e = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                curr += 1
                res = max(res, curr)
            elif start[s] > end[e]:
                e += 1
                curr -= 1
            else:
                s += 1
                e += 1
        return res


                
                







