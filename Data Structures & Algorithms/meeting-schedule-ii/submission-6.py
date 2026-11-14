"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # array of interval objects
        # find min number of rooms req to shcedule all witout conflict
        # max num of overlaps/conflicts at one time
        # 0--10
        #.      10---20
        #.         15---25
        #   5--------20
        # start = 0, 5, 10, 15
        # end   = 10,20,20, 25
        # rooms = 3
    

        if len(intervals) == 0:
            return 0
    
        start = []
        end = []

        for meeting in intervals:
            start.append(meeting.start)
            end.append(meeting.end)

        start.sort()
        end.sort()

        result = 1
        s = 0
        e = 0
        rooms = 1
        for i in range(len(start)):
            if s == len(intervals) - 1:
                return result

            if start[s+1] < end[e]:
                s += 1
                rooms += 1
            elif start[s] == end[e]:
                if start[s] < end[e]:
                    s += 1
                    rooms += 1
                else:
                    e += 1
                    rooms -= 1
            else:
                e += 1
                rooms -= 1
            result = max(result, rooms)
            
        return result
                
                







