class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # integer array of nums, integer k, reutnr k most freq elements
        # bucket array, index = how many times it appears
        # index points to, list nums
        # hashmap key value, key number, value is count
        # create this freq list, 
        # [1, 2, 3, 3]
        # [0, 1, 2, 3, 4]
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result





        