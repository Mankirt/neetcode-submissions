class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b:
            temp = a & b
            a = (a ^ b) & mask
            b = (temp << 1) & mask
        return a if a <= max_int else ~(a ^ mask)