class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        ans = -float('inf')
        for num in nums:   
            if num != ans:
                if c == 0:
                    ans = num
                    c = 1
                else:
                    c -= 1
            else:
                c += 1
        
        return ans