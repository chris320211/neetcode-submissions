"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

        #Input: intervals = [(0,30),(5,10),(15,20)]
        # False
        # Input: intervals = [(5,8),(9,15)]
        # True
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # array of interval objects
        # we know overlap when we compare two
        # first one end time is > the second one start time
        # we need to sort by start time first for that check to work

        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True



        