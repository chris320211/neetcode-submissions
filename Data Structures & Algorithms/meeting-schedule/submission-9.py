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
        # array of meeting time interval objects
        # object has start time and end time
        # determine if they can add all meeting without overlap
        # we know overlap when start time is less than end time

        # sort all meetings by starting time 
        # if 2ndst start time is less than 1stnd end time, overlap
        intervals.sort(key = lambda x: x.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True


        