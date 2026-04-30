"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# intervals = [(0,40),(5,10),(10,20)]
# 0---------------40
#  5-10
#    10-20 return 2
# sort, meetings are sorted
# start: 0 5 15
# end: 10 20 40
# start: 0 5 10
# end: 10 20 40
# start: 0 10
# end: 5 20
# two pointer approach, compare sorted start and sorted end times
# O(nlogn) 
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
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
        result = 0

        while s < len(intervals):
            if end[e] > start[s]:
                count += 1
                s += 1
            elif end[e] == start[e]:
                e += 1
            else:
                count -= 1
                e += 1
            result = max(result, count)
        return result
