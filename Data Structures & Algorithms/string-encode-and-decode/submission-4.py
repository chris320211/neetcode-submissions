class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode length of str, signal
        # hello
        # 5phello
        # p is our signal
        string = ''
        for s in strs:
            string += str(len(s))
            string += 'p'
            string += s
        
        return string

        
    def decode(self, s: str) -> List[str]:
        # length of the string
        # once we see p 
        # 5phello
        result = []
        start = 0
        while start < len(s):
            j = start
            while s[j] != 'p':
                j += 1
            length = int(s[start:j])
            string = s[j + 1: j + 1+length]
            result.append(string)
            start = j + 1 + length
        return result

        