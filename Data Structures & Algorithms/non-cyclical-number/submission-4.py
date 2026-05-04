class Solution:
    def isHappy(self, n: int) -> bool:
        def returnSum(n):
            crr = 0

            while n > 0:
                digit = n%10
                crr += digit * digit
                n = n//10
            return crr
        
        fast = returnSum(n)
        slow = n

        while slow != fast:
            slow = returnSum(slow)
            fast = returnSum(returnSum(fast))
        
        return fast == 1