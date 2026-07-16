class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = dict()
        res = []
        threshold = len(nums) // 3

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 0

        for k, val in count.items():
            if val >= threshold:
                res.append(k)


        return res

        