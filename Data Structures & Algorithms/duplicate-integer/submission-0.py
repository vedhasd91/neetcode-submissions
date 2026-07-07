class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for num in nums:
            if unique.get(num) is None:
                unique[num] = 1
            else:
                unique[num] += 1

        for value in unique.values():
            if value > 1:
                return True
        return False

         