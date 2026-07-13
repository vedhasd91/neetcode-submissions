class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        res = 0
        visited = set()

        l=r=0
        
        while(r < len(s)):
            
            if s[r] not in visited:
                visited.add(s[r])
                r+=1
            else:
                visited.remove(s[l])
                l+=1
            
            res = max(res, r-l)

        return res