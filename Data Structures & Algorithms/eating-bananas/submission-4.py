class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/k)
            return hour <= h
        
        
        l, r = 1 , max(piles)
        res  = max(piles)
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res