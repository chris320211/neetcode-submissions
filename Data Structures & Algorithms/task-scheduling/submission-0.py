import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # array of cpu tasks, int n
        # tasks = ["X","X","Y","Y"], n = 2
        # X Y _ X Y
        # 1 2 3 4 5
        #   2 1 0
        #.    2 1 0
        # freq of tasks, we always want to do most freq
        # maxHeap, always pop the max freq one and do that
        # XXXYY
        # 3x, 2y
        # X
        # queue, tuple (count left, cooldown)
        # 

        counts = {}

        for i in range(len(tasks)):
            if tasks[i] not in counts:
                counts[tasks[i]] = 0
            counts[tasks[i]] += 1
        
        countList = list(counts.values())
        heapq.heapify_max(countList)

        q = deque()
        cycle = 0
        while countList or q:
            cycle += 1
            if len(countList) != 0:
                freq = heapq.heappop_max(countList) - 1
                if freq != 0:
                    q.append((freq, cycle + n))
            
            if len(q) != 0 and q[0][1] == cycle:
                heapq.heappush_max(countList, q.popleft()[0])
        
        return cycle