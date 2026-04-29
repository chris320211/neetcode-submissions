class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array of ints, nums
        # target num = int
        # return INDEX i and j where values associated add up to target
        # i and j are distinct
        # every input has at least one pair of i and j
        
        # brute force
        # no data strucutre involved
        # iterate and compare all combinations

        # example [3, 4, 5, 6], target = 7
        # i = 0 -> 3
        # i = 0 -> 3
        # j = 0 -> 3
        # result = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             result.append(i)
        #             result.append(j)
        #             return result

        # # O(n^2) runtime 
        # # O(1) space

        # better solution
        # utilizing a dict, key and value, key = num and value = index
        # target - nums[i] = nums[j]

        dict = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict: # nums[j] inside dict
                result.append(dict[complement])
                result.append(i)
                return result
            dict[nums[i]] = i

        # O(N) runtime
        # O(N) space
