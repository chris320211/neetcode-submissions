# constructor method
# hashmap = userid -> stationname, t
# hashmap = (start, end) -> [total time, num of trips]
# checkin method (id, stationname, t)
# this id checks in at station at time t
#
# checkout method (id, stationname, t)
# this id checks out at sttion at time t
# time it takes for stationin -> stationout (t - t)
# trip (stations)
# trips complete, so from hashmap we get start station then hash the start end map
# update total time with += difference and += 1 num of trips
# delete from hashtable
# getavgtime(startstation, endstation)
# return avg duration of all compelted trips for that start end pair
# hashmap
# turn input into hashable tuple, then get time and trips, divide return that

class UndergroundSystem:

    def __init__(self):
        self.users = {} 
        self.trips = {}

    def checkIn(self, id, stationName, t):
        pair = (stationName, t)
        if id not in self.users:
            self.users[id] = None
        self.users[id] = pair

    def checkOut(self, id, stationName, t):
        if id not in self.users:
            return
        start = self.users[id][0]
        startT = self.users[id][1]

        tripPair = (start, stationName)
        difference = t - startT

        if tripPair not in self.trips:
            self.trips[tripPair] = [0, 0]
        self.trips[tripPair][0] += difference
        self.trips[tripPair][1] += 1

        del self.users[id]

    def getAverageTime(self, startStation, endStation):
        pair = (startStation, endStation)

        if pair not in self.trips:
            return 0
        else:
            totalTime = self.trips[pair][0]
            totalTrips = self.trips[pair][1]
            average = totalTime / totalTrips
            return average
