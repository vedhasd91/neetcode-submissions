class Solution {
    public boolean isAnagram(String s, String t) {
            char[] sAry = s.toCharArray();
            Arrays.sort(sAry);

        char[] tAry = t.toCharArray();
            Arrays.sort(tAry);

        return Arrays.equals(sAry,tAry);

    }




}
