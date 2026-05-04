class Solution:
    def myPow(self, x: float, n: int) -> float:
        def check(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = check(x , n//2)
            res = res * res

            return res*x if n%2 else res
        
        res = check(x,abs(n))
        return res if n>=0 else 1/res