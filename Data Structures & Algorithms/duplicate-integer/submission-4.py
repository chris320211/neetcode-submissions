class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = nums[i]
                if temp == nums[j]:
                    return True
        return False