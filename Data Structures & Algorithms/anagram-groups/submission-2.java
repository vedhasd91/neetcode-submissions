class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        if(strs == null || strs.length == 0) {
            return new ArrayList<>();
        }
        HashMap<String, List<String>> groupAnagramMap = new HashMap<>();

        for(String str : strs) {
            char[] sortedChars = str.toCharArray();
            Arrays.sort(sortedChars);
            String sortedStr = new String(sortedChars);
            groupAnagramMap.putIfAbsent(sortedStr, new ArrayList<>()); 
            groupAnagramMap.get(sortedStr).add(str);
        }
        return new ArrayList(groupAnagramMap.values());
    }
}
