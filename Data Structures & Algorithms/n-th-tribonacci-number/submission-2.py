class Solution:
    def tribonacci(self, n: int) -> int:
        if n in [0,1]:
            return n
        
        t0= 0
        t1 = 1
        t2 = 1

        for i in range(n-2):
            temp = t2
            t2 += t0 + t1
            t0 = t1
            t1 = temp
        
        return t2
