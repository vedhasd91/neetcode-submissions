class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i+1

        max_prof = 0

        while j < len(prices):
            if prices[j] > prices[i]:
                curr_prof = prices[j] - prices[i]
                max_prof = max(max_prof, curr_prof)
            else:
                i=j
            j+=1
            
        return max_prof

        