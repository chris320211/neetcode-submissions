class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # given an inter array nums, return all triples
        # triples add up to 0
        # output does not have duplicates
        # for loop iterating with i
        # sort
        # [-1,-1,0,1,2]
        # i + j + k == 0
        # j + k = -i
        nums.sort()

        seenSet = set()
        result = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    if tuple([nums[i], nums[j], nums[k]]) not in seenSet:
                        result.append([nums[i], nums[j], nums[k]])
                        seenSet.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
        return result
