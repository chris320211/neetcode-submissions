class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # two arrays nums1 and nums2
        # nums1 is a subset of nums2
        # both have no duplicates
        # for a element in nums1, find the index of it in nums2, and find the greatest
        # elemet to the right

        # brute force
        # result list what is returned
        # for each element in nums1, we find its location i in nums2
        # then we do a check from i and i+1... to find the first greater element
        # add that greater element
        # O(N) O(M) O(M)

        result = []
        indices = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    indices.append(j)
        
        for index in indices:
            for i in range(len(nums2)):
                if i > index and nums2[i] > nums2[index]:
                    result.append(nums2[i])
                    break
            else:
                result.append(-1)
        
        return result
            
            