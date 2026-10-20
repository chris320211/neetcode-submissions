class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use heap with the pairs of num and count
        # pop heap k times so we can ensure we pop k top
        # heap pop log n
        # k * log n

        # can use bucket sort to get o(n)
        # hashmap where we keep track of count of that num
        # list freq, index = count, list at index is the nums that
        # share that same count

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        # for each num and count in key value pair
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        