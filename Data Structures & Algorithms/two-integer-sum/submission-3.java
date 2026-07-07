class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numberMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int currentNumber = nums[i];
            int complement = target - currentNumber;

            if(numberMap.containsKey(complement)) {
                return new int[] {numberMap.get(complement), i};
            }
            numberMap.put(currentNumber, i);
        }
        return null;
    }
}
