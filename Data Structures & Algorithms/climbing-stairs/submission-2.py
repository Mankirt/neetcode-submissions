class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n):
            ans = a+b
            a = b
            b = ans
        return ans