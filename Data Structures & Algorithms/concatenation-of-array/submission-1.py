class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # array nums of len n
        # create an array ans of length 2n
        # first half or ans is nums, second half is same
        # 2x array
        # return answer
        # for loop iterate through entire nums twice
        # for loop append twice
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans