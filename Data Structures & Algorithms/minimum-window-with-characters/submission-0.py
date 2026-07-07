class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t:
            return ""

        tmap = defaultdict(int)
        smap = defaultdict(int)

        for ch in t:
            tmap[ch] += 1

        have, need = 0, len(tmap)

        res, resLen = [-1,-1], math.inf
        l = 0
        
        for r in range(len(s)):

            smap[s[r]]+=1

            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                have += 1

            while have == need:
                window = r - l + 1
                if window < resLen:
                    res = [l, r]
                    resLen = window

                # shrink from left
                smap[s[l]] -= 1
                if s[l] in smap and smap[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != math.inf else ""

        