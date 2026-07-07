class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Step 1: Count frequencies using a HashMap (O(n))
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.merge(num, 1, Integer::sum);
        }

        // Step 2: Create buckets where the index is the frequency (O(n))
        // The size is n + 1 because the maximum frequency can be n
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int i = 0; i < buckets.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        for (int num : frequencyMap.keySet()) {
            int frequency = frequencyMap.get(num);
            buckets[frequency].add(num);
        }

        // Step 3: Collect elements from buckets starting from the highest frequency (O(n))
        List<Integer> result = new ArrayList<>();
        for (int i = buckets.length - 1; i >= 0 && result.size() < k; i--) {
            if (!buckets[i].isEmpty()) {
                for (int num : buckets[i]) {
                    result.add(num);
                    if (result.size() == k) {
                        break;
                    }
                }
            }
        }

        // Convert the List<Integer> to int[]
        return result.stream().mapToInt(i -> i).toArray();
    }
}