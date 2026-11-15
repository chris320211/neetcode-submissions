# design a class to find kth largest int
# stream of integers is array, has duplicates
# min heap of size k, root is min
# add and pop for heap is always o logn
# min val is o(1) peak
# we only keep track of k largest in stream
# while heap is larger than k
# we pop the minimum

# constructor method - k, nums array
# heapify nums
# while len nums is greater than k
# we pop the minimum
# add method - val
# push to heap
# then we remove min

# [3, 2, 7, 8] k = 2
# [7, 8] add 10

import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)
    
    def add(self, val):
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]