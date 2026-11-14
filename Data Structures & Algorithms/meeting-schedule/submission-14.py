"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # array of meeting times
        # add all meetings to schedule, no conflict
        # no overlaps, return bool
        # intervals, any order

        # return false when we find a overlap
        # 0----30
        #  5-10
        # 0-10
        #.     10-20
        #.           30-40
        # curr start is less than prev end return false
        # sort by start time
        # loop

        intervals.sort(key=lambda i:i.start)

        prev = None
        for i in range(len(intervals)):
            if i == 0:
                prev = intervals[i] 
                continue
            if intervals[i].start < prev.end:
                return False
            else:
                prev = intervals[i]
        return True

        # 5--8
        #.    9---15
        # false
            