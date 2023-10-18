import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if h == len(piles):
            return max(piles)
        
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(float(p) / mid)
            if total <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            