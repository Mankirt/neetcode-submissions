class Solution:
    def climbStairs(self, n: int) -> int:
        
        a = 0 
        b = 1
        for i in range(n):
            temp = b
            b = a+b
            a = temp
        
        return b