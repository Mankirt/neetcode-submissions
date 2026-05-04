class Solution:
    def reverseBits(self, n: int) -> int:
        i = 31
        res= 0 
        while n:
            if n%2:
                res+= 2**i
            n = n//2
            i-=1
        return res