"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # person can add all meetings if no overlaps
        # 0-30 i1
        # 30-50 i2 
        # 40-50
        # sort 

        intervals.sort(key=lambda i:i.start)

        for i in range(len(intervals)):
            if i == 0:
                continue
            i1 = intervals[i - 1].end
            i2 = intervals[i].start
            if i2 < i1:
                return False
        return True
            