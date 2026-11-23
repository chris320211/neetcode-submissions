class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # givne string s, find the length of longest substring
        # 'zxyzxyz
        # 3
        # without duplicate, set
        # two pointers, expand the window we look at
        # expand if next one isnt a duplicate, we add to set
        # if there is a duplicate, it exists in our set
        # shrink the window from left, whatever element we remove from set until
        # no mor eduplicates
        # on each iteration we keep track of a counter and update a max
        # 'abcdcbghjk'
        
        seen = set()

        result = 0

        l = 0
        r = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                result = max(len(seen), result)
                r += 1
            else:
                left = s[l]
                seen.remove(left)
                l += 1
        return result
