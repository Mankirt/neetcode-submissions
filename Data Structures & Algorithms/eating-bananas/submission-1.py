class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        avg=int(sum(piles)/len(piles))
        l=1
        r=max(piles)
        res=r
        while l<=r:
            mid=l + (r-l)//2
            hi=0
            for pile in piles:
                hi+=math.ceil(pile/mid)
            if hi<=h:
                res=min(res,mid)
                r= mid-1
            else:
                l=mid+1
        return res
