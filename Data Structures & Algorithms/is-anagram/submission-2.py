class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = defaultdict(lambda: 0)
        
        for c in s:
            char_map[c] += 1 
        
        for c in t:
            if char_map.get(c) == None:
                return False
            char_map[c] -= 1

        for v in char_map.values():
            if v != 0:
                return False
        
        return True