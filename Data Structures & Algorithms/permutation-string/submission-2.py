class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ns1 = len(s1)
        ns2 = len(s2)

        if ns1 > ns2:
            return False
            
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(0, ns1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(ns1, ns2):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i-ns1]) - ord('a')] -= 1

            if count1 == count2:
                return True

        
        return False



        return False

        