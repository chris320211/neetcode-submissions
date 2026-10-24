class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # array of integers heights
        # each value is the height of ith bar
        # the most, i difference x the difference of smallest bar

        area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            new = (j - i) * (min(heights[i], heights[j]))
            if new >= area:
                area = new
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return area