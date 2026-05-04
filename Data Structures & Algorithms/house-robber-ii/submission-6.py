class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def check(arr):
            rob1, rob2 = 0, 0
            for n in arr:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2



        return max(nums[0], check(nums[1:]), check(nums[:-1]))