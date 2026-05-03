class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two integer arrays nums and num1
        # return median, original two arrays r sorted
        # brute force approach
        # we can create a combined list, add them all together and sort
        # then we check if it is odd, its the middle point
        # its even then we do the left and right middle, add, divide by 2

        result = []
        for i in range(len(nums1)):
            result.append(nums1[i])
        for j in range(len(nums2)):
            result.append(nums2[j])
        
        result.sort()
        #1 2 3 4 5
        #len = 5
        #0 1 2

        # 1 2 3 4
        # len = 4
        #  0 1 2 3
        if len(result) % 2 != 0:
            median = result[len(result) // 2]
            return median
        if len(result) % 2 == 0:
            middle_left = (len(result) // 2) - 1
            middle_right = (len(result) // 2)
            median = (result[middle_left] + result[middle_right]) / 2
            return median