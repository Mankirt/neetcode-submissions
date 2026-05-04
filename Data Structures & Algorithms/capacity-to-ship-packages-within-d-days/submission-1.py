class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def day(n):
            d = 0
            temp = n
            for wt in weights:
                if wt <= temp:
                    temp -= wt
                else:
                    d+=1
                    temp = n - wt
            return d+1
        r = sum(weights)
        l = max(weights)
        res = r
        while l <= r:
            m = l + (r-l)//2
            if day(m)<=days:
                r = m - 1
                res = min(res,m)
            else:
                l = m+1
        return res
        
