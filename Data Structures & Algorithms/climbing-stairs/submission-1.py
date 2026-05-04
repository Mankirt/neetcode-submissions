class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        a =1
        b =2
        i=3
        while i<=n:
            ans = a+b
            a=b
            b=ans
            i+=1
        return ans