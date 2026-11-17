# 3 diff types of spaces
# big med small
# 3 ints count of spaces avail
# if carType = 1
# check big, if it is 0, return False, otherwise return true
# 3x

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big == 0:
                return False
            else:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium == 0:
                return False
            else:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small == 0:
                return False
            else:
                self.small -= 1
                return True
