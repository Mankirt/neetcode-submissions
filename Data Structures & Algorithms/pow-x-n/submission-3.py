class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        dp = {2:x*x, 0: 1}
        def find(n):
            
            if n in dp:
                return dp[n]
            
            if n%2 :
                result = find(n-1) * x
            else:
                result = find(n//2) * find(n//2)
            
            dp[n] = result

            return result
        res = find(abs(n))
        return res if n>0 else 1/res