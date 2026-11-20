class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # two arrays position and speed where index represents car
        # destination is target
        # car cannot pass one ahead can only catch up and match speed
        # car fleet is cars same positon and same speed
        # return diff car fleets that will arrive at destination
        # we want to find when they intersect
        # if they intersect, we keep the one ahead's speed and treat as 1 car fleet
        # check from right to left, closer to target first
        # for two cars, check time it takes to get there
        # if the one behind takes less time they are going to collide
        # using a stack, add first car to stack, then add next car to stack
        # compare the two cars on stack if they collide
        # we pop the top one
        
        cars = []
        for i in range(len(position)):
            pair = (position[i], speed[i])
            cars.append(pair)
        
        cars.sort(key=lambda i:i[0], reverse=True)
        stack = []
        for i in range(len(cars)):
            position = cars[i][0]
            speed = cars[i][1]
            distance = target - position
            time = distance / speed
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # collision so combine to one car fleet
                stack.pop()
        
        return len(stack)
            

            
        