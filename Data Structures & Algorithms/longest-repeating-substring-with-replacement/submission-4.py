class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        freq = defaultdict(int)

        # Crux windowLen - Count[MostFreqChar] <= k
        while r < len(s):
            freq[s[r]] += 1
            maxf = freq[max(freq, key=freq.get)]

            while (r - l + 1 - maxf) > k:
                freq[s[l]] -= 1
                l+=1

            res = max(res, r - l + 1)
            r+=1
            
            
            #print(l,r, res)
            
        
        return res