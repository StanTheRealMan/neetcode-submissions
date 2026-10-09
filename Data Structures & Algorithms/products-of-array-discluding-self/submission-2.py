class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes, prod = 0, 1
        res = [0] * len(nums)
        for n in nums:
            if not n:
                zeroes += 1
                if zeroes > 1:
                    return res
            else:
                prod *= n
        
        for i, n in enumerate(nums):
            if zeroes:
                res[i] = 0 if n else prod
            else:
                res[i] = prod // n
        return res
        
