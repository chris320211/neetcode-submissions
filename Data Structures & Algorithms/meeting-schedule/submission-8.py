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

        # brute force 
        # we check each pair
        # overlap when earlier ending time is greater than later start time
        # example : (0,30) (5,10) overlap since 
        # earlier end time is 30
        # later start time is 5
        # 30 > 5 so overlap
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)):
            if i + 1 < len(intervals):
                if intervals[i].end > intervals[i+1].start:
                    return False
        return True
            
            # sort by start time
            # 


        