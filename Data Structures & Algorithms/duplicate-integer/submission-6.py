class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #brute force. O(n^2) time complex, O(1) space complex
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         temp = nums[i]
        #         if temp == nums[j]:
        #             return True
        # return False

        #algorithm way (sorting) O(nlogn) time complex, space complex O(n) 
        # nums.sort() # sorts in increasing order (1,2,3,3,4)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        #hash way
        seen = set() #putting already seen values into the set
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False