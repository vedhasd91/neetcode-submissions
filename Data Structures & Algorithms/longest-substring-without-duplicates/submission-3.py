class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        l = 0
        r = 0
        slen = 0

        while r < len(s):
            if s[r] in visited:
                l = max(visited[s[r]]+1,l)
            visited[s[r]] = r
            slen = max(slen, r-l+1)
            print(l,r,s[l],s[r])
            r+=1

        return slen
