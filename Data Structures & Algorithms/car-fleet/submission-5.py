class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars
        # target is their respective positions
        # speed is their respective speeds
        # index represents the car
        # we want to determine how many car fleets reach target
        # car fleet is when a car meets each other so same distacne at same time
        # use a stack to keep track of fleets
        # pair pos and speed, sort by pos
        # (pos, speed)
        # we need to find out when they intersect
        # we can take the time to target, if this one starts less, less time, we
        # know it becomes a car fleet
        # we keep the lower speed in the stack
        # iterate from greatest pos to least
        # stack (time)
        cars = []
        for i in range(len(position)):
            pair = (position[i], speed[i])
            cars.append(pair)
        cars.sort(key=lambda i:i[0], reverse=True)

        stack = []
        for i in range(len(cars)):
            distance = target - cars[i][0]
            time = distance / cars[i][1]
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)
                
        
            

            
        