class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")

        j = len(s) - 1
        i = 0

        while i < j:
            while j>i and not s[j].isalnum():
                j-=1
            while i<j and not s[i].isalnum():
                i+=1
            
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
