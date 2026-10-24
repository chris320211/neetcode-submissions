class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # integer array nums, return three nums where
        # all three sum up to 0
        # maybe we can sort first?
        # brute force is three loops
        # MUST SORT n log n, then we keep track of a, two pointer
        # if next a is equal to prev a then we skip

        res = []
        nums.sort()
        for x in range(len(nums)):
            a = nums[x]
            if x > 0 and a == nums[x - 1]:
                continue
            i = x + 1
            j = len(nums) - 1
            while i < j:
                if a + (nums[i] + nums[j]) == 0:
                    res.append([a, nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif a + (nums[i] + nums[j]) < 0:
                    i += 1
                elif a + (nums[i] + nums[j]) > 0:
                    j -= 1
        return res
