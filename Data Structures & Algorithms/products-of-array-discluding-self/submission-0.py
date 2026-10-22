class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix [1, 1, 2, 8]
        # postfix [48, 24, 6, 1]
        # O(1) space


        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix = postfix * nums[i]
        
        return res
