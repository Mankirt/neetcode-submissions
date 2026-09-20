class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 1:
            temp = 0
            while n > 0:
                a= n%10
                temp += a*a
                n //= 10
            if temp in s:
                return False
            s.add(temp)
            n = temp
        return True
