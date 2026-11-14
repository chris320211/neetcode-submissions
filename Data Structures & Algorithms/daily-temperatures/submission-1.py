class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array of temp, ith index represents ith day
        # return result, how many indices it takes to see a warmer temp
        # if nothing ahead we set it to 0
        # stack = [0, ]
        # temperatures = [30,38,30,36,35,40,28]
        # if stack is empty, we add
        # [1, 4, 1, 2, 1, 0, 0]
        # stack is keeping track of indicies
        #

        result = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                diff = i - index
                result[index] = diff
            stack.append(i)
        return result

        




