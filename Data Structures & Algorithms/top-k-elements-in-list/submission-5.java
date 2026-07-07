class Solution {
    public int[] topKFrequent(int[] nums, int k) {
   
        // count the frequencies
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for(int num : nums) {
            freqMap.merge(num, 1, Integer::sum);
        }

        //create buckets
        List<Integer>[] buckets = new List[nums.length+1];
        for(int i=0; i < buckets.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        // map frequenceis to buckets 
        for(int num: freqMap.keySet()) {
            int frequency = freqMap.get(num);
            buckets[frequency].add(num);
        }
        

        //create result and fetch buckets in to it
        List<Integer> result = new ArrayList<>();
        for(int i = buckets.length-1; i >=0 && result.size() < k; i--) {
            if(!buckets[i].isEmpty()) {
                for(int num : buckets[i]) {
                    result.add(num);
                    if(result.size() == k) {
                        break;
                    }
                }
            }
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}