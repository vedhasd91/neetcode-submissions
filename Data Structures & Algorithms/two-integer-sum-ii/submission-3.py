class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        h = len(numbers) - 1

        res = []

        while l < h:
            _sum = numbers[l] +  numbers[h]

            if _sum > target:
                h -= 1
            elif _sum < target:
                l += 1
            else:
                res.append(l+1)
                res.append(h+1)
                return res
        
        return res