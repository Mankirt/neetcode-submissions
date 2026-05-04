class Solution:
    def isHappy(self, n: int) -> bool:
        
        def integer_sum(i):
            crr = 0
            while i>0:
                d = i%10
                i = i//10
                crr += d*d
            return crr
        s = {n}
        while n!=1:
            n = integer_sum(n)
            if n in s:
                return False
            s.add(n)

        return True