class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # distinct array of nums
        # sorted in ascneding
        # target in
        # search function to return index of target within nums
        # if not there return -1
        # binary search

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1