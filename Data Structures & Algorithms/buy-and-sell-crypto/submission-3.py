class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        i, j = 0, 1

        while j < len(prices):

            res = prices[j] - prices[i]

            if res >= 0:
                profit = max(profit, res)
                j+=1
            else:
                i=j


        return profit
        