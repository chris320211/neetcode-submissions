class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array num and target int
        # return index i and j where num[i] + num[j] == target
        # return as list
        # one pair must exist
        # we can go thru list, store complement, 
        # if complement is in, we return indexes
        # hashmap to store index and complement

        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                temp = dict[nums[i]]
                return [temp, i]
            complement = target - nums[i]
            if complement not in dict:
                dict[complement] = i