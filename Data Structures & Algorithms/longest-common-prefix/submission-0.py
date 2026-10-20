class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # given array of strings strs
        # return the longest ocmmon prefix of all strings
        # no common prefix return ""

        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]  
        return res