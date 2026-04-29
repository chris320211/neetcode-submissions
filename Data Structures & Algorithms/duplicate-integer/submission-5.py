class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         temp = nums[i]
        #         if temp == nums[j]:
        #             return True
        # return False

        #algorithm way (sorting)
        nums.sort() # sorts in increasing order (1,2,3,3,4)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False