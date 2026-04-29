class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # array prerequisites, inside [a,b], b is the prereq to a
        # [0, 1], need to take course 1 before course 0
        # a, b are integers
        # numCourses = 3 classes: 0, 1, 2
        # [0,1] and [1,0] is False, contradiction

        # kahn's algorithm topological sort with BFS
        # can I keep finding courses with zero remaining prereqs
        # if yes true, if no false

        graph = []
        for i in range(numCourses):
            graph.append([])
        # graph index is the prereq, list is what it unlocks
        inDegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            inDegree[crs] += 1
        # indegree incremeted since course crs depends on a prereq

        # find courses with no prereqs, starting courses we take
        queue = []
        for c in range(numCourses):
            if inDegree[c] == 0:
                queue.append(c)
        
        head = 0
        coursesTaken = 0

        while head < len(queue):
            currentCourse = queue[head]
            head += 1
            coursesTaken += 1
            
            for nextCourse in graph[currentCourse]:
                inDegree[nextCourse] -= 1
                
                # If a course now has zero remaining prereqs, it's ready
                if inDegree[nextCourse] == 0:
                    queue.append(nextCourse)
        
        # Step 4: Check the result
        # If we took every course, there was no cycle
        # If some courses got stuck (cycle), coursesTaken will be less
        return coursesTaken == numCourses


