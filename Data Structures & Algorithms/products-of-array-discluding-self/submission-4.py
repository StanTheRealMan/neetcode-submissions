class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes, prod = 0, 1
        res = [0] * len(nums)

        for n in nums:
            if n == 0:
                if zeroes:
                    return res
                else:
                    zeroes += 1
            else:
                prod *= n
        
        if zeroes:
            for i, n in enumerate(nums):
                if not n:
                    res[i] = prod
                    return res

        for i, n in enumerate(nums):
            res[i] = prod // n
        
        return res