class Solution:
    def reorganizeString(self, s: str) -> str:

        res = ""
        freq = defaultdict(int)

        for i in range(len(s)):
            freq[s[i]] += 1

        mostfreq = [(-f, ch) for ch, f in freq.items()]

        heapq.heapify(mostfreq)

        prev = None
        while mostfreq or prev:
            
            if prev and not mostfreq:
                return ""

            cnt, ch = heapq.heappop(mostfreq)

            res+=ch
            cnt += 1

            if prev:
                heapq.heappush(mostfreq, prev)
                prev = None
            
            if cnt != 0:
                prev = (cnt, ch)
            
        return res