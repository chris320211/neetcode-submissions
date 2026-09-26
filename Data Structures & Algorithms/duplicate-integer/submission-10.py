class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # array nums
        # return bool, true if appear more than once
        # hash set to keep track, if num already in, return

        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])

        return False
    