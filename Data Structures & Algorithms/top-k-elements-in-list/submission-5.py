class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # integer array nums, an integer k
        # return k most freq elements
        # bucket sort
        # hashmap of count, build hashmap
        # 2d array where each index value is a bucket
        # key num, value is count
        # [bucket] = nums
        # index = count
        # [1, 2, 2, 3, 3]

        stat = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n not in stat:
                stat[n] = 0
            stat[n] += 1
        
        for num, count in stat.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, -0, -1):
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res







        