from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = h

        while l <= r:
            m = (l + r) // 2
            cur = 0
            
            for pile in piles:
                cur += ceil(pile / m)
            
            if cur <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
            