class Solution:
    def rob(self, nums: List[int]) -> int:
        def find(arr):
            a = 0 
            b = 0
            for num in arr:
                temp = max(a+num,b)
                a = b
                b = temp
            return b
        
        return max(nums[0], find(deepcopy(nums[1:])), find(deepcopy(nums[:-1])))