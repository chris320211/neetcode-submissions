class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # integer array called heights [1, 2, 6...]
        # heights[i] is height of ith bar makes sense
        # choose two bars to form a container
        # return max amount of water
        # max amount of water = index diff * lowest height
        # two pointer front and back

        front = 0
        back = len(heights) - 1
        max = 0
        while front < back:
            area = (back - front) * min(heights[front], heights[back])
            if area >= max:
                max = area
            # way to advance two pointers
            # we want to find the shorter bar
            # if we advance from shorter bar we can potentially get larger
            if heights[front] <= heights[back]:
                front = front + 1
            else:
                back = back - 1
        return max