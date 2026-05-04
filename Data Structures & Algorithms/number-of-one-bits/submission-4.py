class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n & 1
            n = n >> 1
        return res
        
        res= 0 
        while n > 0:
            res += n%2
            n //= 2
        return res