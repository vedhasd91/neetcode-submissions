class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        visited_ = {}

        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if visited_.get(sorted_word) is not None:
                visited_.get(sorted_word).append(word)
            else:
                visited_[sorted_word] = [word]
        
        return [string for string in visited_.values()]