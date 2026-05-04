class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = r
        def check(m):
            i = 0
            count = 0
            while i < len(weights):
                temp = m
                while temp > 0:
                    if i<len(weights) and weights[i] <= temp:
                        temp -= weights[i]
                        i+=1
                    else:
                        break
                count +=1
            if count <= days:
                nonlocal ans
                ans = min(ans,m)
                return True
            else:
                return False
        while l <= r:
            m = l +(r-l)//2
            if check(m):
                r = m-1
            else:
                l = m+1
        
        return ans

