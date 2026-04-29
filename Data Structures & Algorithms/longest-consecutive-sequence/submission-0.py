class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # array of integers
        # return lenght of longest consecutive sequence of elements
        # example [2,3,4,5, 100]
        # returned 4

        # sorting the nums
        # checking each as soon as we see a non +1, we reset the count

        if len(nums) == 0:
            return 0
        
        nums.sort()
        count = 1
        result = 1
        for i in range(len(nums) - 1):
            if (nums[i + 1] - nums[i]) == 0:
                continue
            if (nums[i + 1] - nums[i]) != 1:
                result = max(count, result)
                count = 1
            else:
                count += 1
        return max(count, result)