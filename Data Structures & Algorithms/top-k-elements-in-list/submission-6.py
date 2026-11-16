class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given integer array nums
        # inter k
        # return the k most freq elements

        counts = {}

        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        
        keys = sorted(counts.keys(), key = counts.get, reverse=True)
        return keys[:k]







        