class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array of integers temperatures where ith represent daily temp
        # return result array, value is num of days after
        # the ith day before a warmer temp appears
        # if there is no warmer it is 0
        # stack, 
        result = [0] * len(temperatures)
        stack = [] # pair of value with index [temp, index]
        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append([temperatures[i] , i])
        return result