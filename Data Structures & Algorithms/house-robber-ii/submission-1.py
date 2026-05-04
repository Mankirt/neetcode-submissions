class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        def check(arr):
            last = 0
            nxt = 0

            for num in arr:
                temp = max(nxt,last+num)
                last = nxt
                nxt = temp
            return nxt

        return max(nums[0],check(nums[:-1]),check(nums[1:]))