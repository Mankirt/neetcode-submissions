class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
           

        def check(i,total):
            if i==len(nums):
                return total
            return check(i+1,total^nums[i]) + check(i+1,total)

        return check(0,0)