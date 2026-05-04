class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n & (n-1) == 0:
                return res + 1
            res += 1
            n = n & (n-1)
        return res