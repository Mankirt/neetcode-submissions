class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        d[nums[0]]=0
        for i in range (1,len(nums)):
            if target - nums[i] in d:
                return [d[target-nums[i]],i]
            d[nums[i]]=i