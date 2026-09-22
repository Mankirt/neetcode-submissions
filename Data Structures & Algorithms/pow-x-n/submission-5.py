class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def check(a,n):
            if a == 0:
                return 0
            if n == 0:
                return 1
            res = check(a*a,n//2)
            return res*a if n%2 else res
        
        res = check(x,abs(n))
        return res if n >=0 else 1/res
        