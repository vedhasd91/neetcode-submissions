class Solution {
    public int lengthOfLongestSubstring(String s) {
        int lp = 0;
        int len = 0;
        HashSet<Character> charSet = new HashSet<>();

        for(int r = 0; r < s.length(); r++) {

            while(charSet.contains(s.charAt(r))) {
                charSet.remove(s.charAt(lp));
                lp++;
            }
            charSet.add(s.charAt(r));
            len = Math.max(r-lp+1, len);
        }
        return len;
    }
}
