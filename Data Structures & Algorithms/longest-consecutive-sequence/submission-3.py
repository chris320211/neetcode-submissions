class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # array of nums, return longest consectuve seq
        # set check -1 +1 value is in set
        # num - 1 isnt in set, we know possible start of seq
        # 
        numSet = set(nums)
        count = 0
        for n in nums:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                if length > count:
                    count = length
        
        return count
                