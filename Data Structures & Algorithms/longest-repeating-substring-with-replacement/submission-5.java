class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;

        HashSet<Character> charSet = new HashSet<>();
        for (char c : s.toCharArray()) {
               charSet.add(c); 
        }

        for(char c : charSet) {
            int count= 0, lp = 0;
            for(int r=0;  r < s.length(); r++) {
                    if(s.charAt(r) == c) {
                        count++;
                    }

                    while((r -lp +1) - count > k ) {
                        if(s.charAt(lp) == c) {
                            count--;
                        }
                        lp++;
                    }

                    res = Math.max(res, (r-lp+1));
            }
        }
        return res;
    }
}
