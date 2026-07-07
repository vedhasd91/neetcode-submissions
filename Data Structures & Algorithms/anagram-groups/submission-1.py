class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        visited_ = defaultdict(list)

        for word in strs:
            hashmap = [0] * 26
            for c in word:
                hashmap[ord(c)-ord('a')] += 1

            visited_[tuple(hashmap)].append(word)
        
        return [string for string in visited_.values()]