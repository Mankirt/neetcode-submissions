class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n==1:
            return n
        if n == 2:
            return 1
        t1, t2, t3 = 0, 1, 1
        for i in range(3,n+1):
            temp = t1+t2+t3
            t1 = t2
            t2 = t3
            t3 = temp
        return t3