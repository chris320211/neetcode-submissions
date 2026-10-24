class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode a list of strings into a single string
        # 5#Hello5#World

        res = ''
        for s in strs:
            length = str(len(s))
            res += length
            res += 'W'
            res += s
        return res

        
    def decode(self, s: str) -> List[str]:
        # once count is reached, read the next count
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "W":
                j += 1
            length = int(s[i:j])
            temp = s[j + 1 : j + 1 + length]
            res.append(temp)
            i = j + 1 + length
        return res