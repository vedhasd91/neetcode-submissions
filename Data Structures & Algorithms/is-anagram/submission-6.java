class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) {
            return false;
        }

        int[] chars = new int[256];
        s = s.toLowerCase();
        t = t.toLowerCase();

        for(char c : s.toCharArray()) {
            chars[c]++;
        }

        for(char c : t.toCharArray()) {
            chars[c]--;
            if(chars[c] <0) {
                return false;
            }
        }
        return true;
    }
}
