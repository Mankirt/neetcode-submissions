class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        i = len(digits) - 1
        while i>=0:
            if digits[i] + 1 >= 10:
                digits[i] = (digits[i] + 1) % 10
            else:
                digits[i] += 1
                return digits
            i-= 1
        
        return [1] + digits
                