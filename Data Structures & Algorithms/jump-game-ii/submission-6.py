class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l = 0
        r = 0
        farthest = 0
        steps = 0
        while r < len(nums) - 1:
            while l <= r:
                farthest = max(farthest, l + nums[l])
                l+=1
            r = farthest
            steps += 1
        return steps