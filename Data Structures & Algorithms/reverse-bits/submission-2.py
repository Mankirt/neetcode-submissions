class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        i = 0
        while n != 0:
            if n%2:
                out += 2**(31-i)
            i+=1
            n = n//2
        return out