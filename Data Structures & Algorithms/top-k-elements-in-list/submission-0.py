class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # integer array nums
        # integer k
        # return the k most frequenet elemtns in that array
        # example: [1, 2, 2, 3, 3], k = 2
        # return [2,3] since the are the two most frequent
        
        # hashmap dictionaary, key is int, value as count
        # sort by the count, return the top k

        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
        
        # cannot sort a dict, we need to get all elements as a list
        sorted_pairs = sorted(dict.items(), key=lambda p: p[1], reverse = True) #p[1] is the freq since (key, freq)
        top_k_pairs = sorted_pairs[:k] # 0, 1, not including k
        result = []
        for i in range(len(top_k_pairs)):
            result.append(top_k_pairs[i][0])
        return result