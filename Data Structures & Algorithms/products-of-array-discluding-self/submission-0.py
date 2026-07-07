class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []

        prefix = []
        product = 1
        for i in range(0, len(nums)):
            product *= nums[i]
            prefix.append(product)

        postfix = []
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix.insert(i//(len(nums)-1),product)

        print(prefix, postfix)
        
        pr = 1
        po = 1
        for i in range(0, len(nums)):
            if i-1 < 0:
                pr = 1
                po = postfix[i+1]
            elif i+1 >= len(nums):
                pr = prefix[i-1]
                po = 1
            else:
                pr = prefix[i-1]
                po = postfix[i+1]
    
            res.append(pr*po)

        return res
        