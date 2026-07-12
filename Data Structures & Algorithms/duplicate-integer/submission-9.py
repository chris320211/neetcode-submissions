class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # integer array of nums
        # return true if any value appears more than once
        # hashset to keep track of existence
        # if element in hashset already we return true
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            