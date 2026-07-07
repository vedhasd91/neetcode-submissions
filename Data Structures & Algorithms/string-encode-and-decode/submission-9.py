class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for st in strs:
            encoded_str += str(len(st)) + '#' + st
            
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        
        while i < len(s):
            lt = 0
            while s[i] != '#':
                lt = 10*lt + int(s[i])
                i += 1

            i += 1
            j = i+lt
            strs.append(s[i:j])
            i = j

        return strs