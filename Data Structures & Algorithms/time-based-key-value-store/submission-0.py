# time base key value daa strucutre
# store multiple values for same key at diff time stamps
# retrieve keys value at certain timestamp

# constructor method
# hashmap
# key maps to a array
# array of pair (time, value)
# all timestamps of set are increasing, sorted

# set method
# stores the key with the value at given time
# create our pair
# check if key is in
# if not we create empty array
# add our pair

# get method
# retruns a value where set was done before that timestamp
# if multiple sets values with that key, we return the one with largest stamp
# if no values returns empty string
# search for the specific timestamp
# binary search logn
# if not we jus return the next greatest

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        pair = [timestamp, value]
        if key not in self.store:
            self.store[key] = []
        self.store[key].append(pair)
    def get(self, key, timestamp):
        res = ''
        if key not in self.store:
            return res
        values = self.store[key]

        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            elif values[mid][0] > timestamp:
                r = mid - 1
        return res


        
