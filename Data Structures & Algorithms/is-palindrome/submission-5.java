class Solution {
    public boolean isPalindrome(String s) {

        int leftPointer = 0;
        int rightPointer  = s.length()-1;

        while (leftPointer < rightPointer)  {

               while(leftPointer < rightPointer && !isAlphaNum(s.charAt(leftPointer))) {
                    leftPointer++;
               }

               while(rightPointer > leftPointer && !isAlphaNum(s.charAt(rightPointer))) {
                    rightPointer--;
               }

               if(Character.toLowerCase(s.charAt(leftPointer)) !=
                Character.toLowerCase(s.charAt(rightPointer)) ) {
                    return false;
                }
                leftPointer++; rightPointer--;
        }
        return true;
    }

    public boolean isAlphaNum(char c) {
        return (c >= 'A' && c <= 'Z') ||
            (c >= 'a' && c <= 'z') ||
            (c >= '0' && c <= '9');
       }
}
