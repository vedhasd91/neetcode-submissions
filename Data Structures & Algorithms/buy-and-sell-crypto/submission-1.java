class Solution {
    public int maxProfit(int[] prices) {
        int lp = 0, rp = 1;
        int profit = 0;

        while (rp < prices.length) {
            if(prices[lp] < prices[rp]) {
                int profitPt = prices[rp] - prices[lp];
                profit = Math.max(profitPt, profit);
            } else {
                lp = rp;
            }
            rp++;
        }
    return profit;       
    }
}
