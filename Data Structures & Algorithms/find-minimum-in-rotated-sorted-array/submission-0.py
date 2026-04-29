class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array of length n
        # if we rotate n times we get original
        # O(logn) binary search problem
        # binary search only works when sorted

        # we need to find the pivot point so when
        # nums[i] > nums[i+1]

        length = len(nums)
        left = 0 
        right = length - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]




        


        