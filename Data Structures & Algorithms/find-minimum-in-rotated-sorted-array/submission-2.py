class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = nums[0]

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < min_num:
                min_num = nums[m]
                r = m - 1
            else:
                l = m + 1
        return min_num