class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        j = i + 1

        max_prof = 0

        while j<len(prices):

            if prices[j] > prices[i]:
                # profit
                curr = prices[j] - prices[i]
                max_prof = max(curr, max_prof)
            else:
                # buy on new day
                i=j
            j+=1
        

        return max_prof