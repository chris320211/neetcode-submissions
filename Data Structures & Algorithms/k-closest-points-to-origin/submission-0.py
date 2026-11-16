import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sd array points
        # points[i] is the cordinates for point i
        # return the k closest points to orgin
        # 0,0 to x1, y2 distance
        # distance for each x1,y2
        # k closest points means distance to origin is smallest
        # heap, use a minheap
        # 
        # empty array
        # for each element, we create the pair
        # calculate the distance for each
        # (distance, [cordinate]), we push it on to the heap

        # return is k times we pop
        # popped[1].append
        # heap node = tuple, (distance, [cordinates])

        minHeap = []

        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = 0
            y2 =0
            distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            pair = (distance, [x1, y1])
            heapq.heappush(minHeap, pair)

        result = []

        for i in range(k):
            popped = heapq.heappop(minHeap)
            result.append(popped[1])

        return result
            
        
