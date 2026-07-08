class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            temp = b
            b = max(num + a , b)
            a = temp
        
        return max(a,b)