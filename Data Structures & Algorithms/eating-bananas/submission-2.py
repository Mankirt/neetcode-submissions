class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        def check(m):
            res = 0
            for pile in piles:
                res += math.ceil(pile/m)
            return res

        while l<=r:
            m = l + (r-l)//2
            if check(m) <=h:
                res = min(res,m)
                r = m - 1
            else:
                l = m + 1
        return res


        
