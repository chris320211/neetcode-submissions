class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # given an array of prereqs
        # prereq[i] = [a, b]
        # must take b first to take a
        # a -> b
        # numCourses - 1 is the max course num from 0
        # return true if can finish all courses
        # false if we want
        # [0,1] [1,2] [2,3] [2,4] [3,4]
        # 0 -> 1 -> 2 -> 3----->4
        #             --------->4 -> 0
        # hashmap key is the course, value is list of prereqs
        # key value
        #  0.  [1]
        # 1     [2]
        #  2    [3,4]
        #  3.    [4]
        # 
        # dfs 
        # visitSet, if the ocurse in visit set is hit, we know its loop return false
        # O(N+P)
        preMap = { i: [] for i in range(numCourses)}

        for i in range(len(prerequisites)):
            crs = prerequisites[i][0]
            pre = prerequisites[i][1]

            if crs not in preMap:
                preMap[crs] = []
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visitSet:
                return False
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) is False:
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True

