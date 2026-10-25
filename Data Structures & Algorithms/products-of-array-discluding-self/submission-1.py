class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # integer array nums
        # return output array
        # [1,2,4,6]
        # prefix [1,2,8,48]
        # postfix [48,48,24,6]
        # check if beg or end of nums

        prefixList = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            prod = prefix * nums[i]
            prefixList[i] = prod
            prefix = prod

        postfixList = [1] * len(nums)
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            prod = postfix * nums[i]
            postfixList[i] = prod
            postfix = prod

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(postfixList[i+1])
            elif i == (len(nums) - 1):
                result.append(prefixList[i - 1])
            else:
                product = prefixList[i - 1] * postfixList[i + 1]
                result.append(product)
        
        return result
            

