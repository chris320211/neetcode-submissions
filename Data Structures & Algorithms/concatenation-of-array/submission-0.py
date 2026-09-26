class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # two int array nums of len n
        # create array ans, len 2n
        # ans [i] == nums [i]
        # ans[i + n] == [i]
        # first half is copy
        # second half is also a copy
        # need to intiate empty list of 2n
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans