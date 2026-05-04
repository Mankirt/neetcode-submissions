class Solution:
    def isHappy(self, n: int) -> bool:
        
        def integer_sum(i):
            crr = 0
            while i>0:
                d = i%10
                i = i//10
                crr += d*d
            return crr
        slow, fast = n, integer_sum(n)

        while slow!=fast:
            fast = integer_sum(integer_sum(fast))
            slow = integer_sum(slow)
        
        return fast == 1