class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def find(arr):
            rob1, rob2 = 0, 0 
            for house in arr:
                temp = rob2
                rob2 = max(house + rob1, rob2)
                rob1 = temp
            return rob2
        
        return max(find(nums[1:]), find(nums[:-1]), nums[0])