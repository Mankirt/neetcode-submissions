class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1,-1,-1):
            new_sum = digits[i] + carry
            digits[i] = new_sum%10
            carry = new_sum//10
            if carry ==0:
                break
        
        return [1]+digits if carry else digits