class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # string s, return the length of longest substring
        # longest substring w/o duplciate char
        # s is only ASCII characters
        # continuous substring w/o duplicate char

        current_str = ""
        count = 0
        max = 0
        for i in range(len(s)):
            if s[i] not in current_str:
                current_str = current_str + s[i]
                count = count + 1
                if count > max:
                    max = count
            elif s[i] in current_str:
                if count > max:
                    max = count
                dup_idx = current_str.index(s[i])
                current_str = current_str[dup_idx + 1:] + s[i]
                count = len(current_str)
        return max
            # 'aab'
            # 1: "a" c = 1
            # 2: "aa" -> "" max = 1 c = 0
            # 3: "" -> "" max = 2 c = 0 
            # 4: "k" c='
        
            
        