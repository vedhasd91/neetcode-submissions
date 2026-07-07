class Solution {
    public int maxArea(int[] heights) {
        int lp = 0;
        int rp = heights.length-1;
        int resArea = 0;

        while (lp < rp) {
            int area = Math.min(heights[lp], heights[rp]) * (rp - lp);
            resArea = Math.max(resArea, area);

            if(heights[lp] < heights[rp]) {
                lp++;
            } else {
                rp--;
            }
        }
        return resArea;
    }
}
