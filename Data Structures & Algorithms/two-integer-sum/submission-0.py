class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complementary = target - num
            if complementary in seen:
                return [seen[complementary], i]
            seen[num] = i