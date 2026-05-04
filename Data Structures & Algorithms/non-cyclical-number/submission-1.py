class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        def check(n):
            ans = 0
            while n>0:
                a = n%10
                ans += a*a
                n=n//10
            
            return ans

        slow, fast = n, check(n)
        while slow!=fast:
            fast = check(fast)
            fast = check(fast)
            slow = check(slow)
            if fast == 1:
                return True
        return False

    
    