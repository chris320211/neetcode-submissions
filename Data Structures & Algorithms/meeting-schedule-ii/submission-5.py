"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # maximum overlapping meetings
        # count = overlapping meeting, 
        # two pointer, two arrays
        # start array [0 10 15]
        # end array [10 20 40]

        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        start.sort()
        end.sort()

        s = 0
        e = 0

        count = 0
        res = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(count, res)
        return res
    





