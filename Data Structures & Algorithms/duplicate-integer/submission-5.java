class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();
        for(int num: nums) {
            numSet.add(num);
        }

        if(nums.length == numSet.size()) {
            return false;
        } else {
            return true;
        }

    }
}