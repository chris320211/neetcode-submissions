class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # array of nums
        # return len of longest consev seq of ints
        # check if that number - 1 exists
        # hashset o(1) lookup
        # if that number is start
        # while num in set:
        # keep count
        # num += 1
        # after while loop returns
        # see if this count is more than our res count

        res = 0
        numSet = set(nums)

        for i in range(len(nums)):
            count = 0
            curr = nums[i]
            if curr - 1 not in numSet:
                while curr in numSet:
                    count += 1
                    curr += 1
            res = max(count, res)
        
        return res