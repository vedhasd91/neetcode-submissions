class Solution {
    public int[] productExceptSelf(int[] nums) {

        int aryLen = nums.length;
        int[] res = new int[aryLen];

        res[0] = 1;
        for(int i=1; i<aryLen; i++) {
            res[i] = res[i-1] * nums[i-1];
        }

        int postFix = 1;
        for(int i = aryLen-1; i >=0; i--) {
            res[i] *= postFix;
            postFix *= nums[i];
        }

        return res;
    }
}  
