class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(n):
            hr = 0
            for pile in piles:
                hr += math.ceil(pile/n)
            return hr
        
        r = max(piles)
        l = 1
        res = max(piles)
        while l <= r:
            m = l + (r-l)//2
            hr = hours(m)
            if  hr <= h:
                res = min(res,m)
                r = m - 1
            else:
                l = m + 1
        
        return res