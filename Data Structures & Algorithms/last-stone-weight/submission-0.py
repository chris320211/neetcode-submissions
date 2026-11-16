import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # array of stones
        # on each step, choose two heaviest
        # weight x and y
        # smash them together
        # if x == y, both are removed
        # if x < y, then x is destroyed
        # y new weight = y - x
        # max heap
        # pop the max out
        # each step we pop twice, 2x logn
        # add a new one
        # while len stones > 1
        # two pops
        # do our checks, maybe we destroy all, add a new one
        # return stones[0

        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x == y:
                continue
            elif x > y:
                new = x - y
                heapq.heappush_max(stones, new)
            
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]
