class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        l = 0
        r = nums[0]
        farthest = r
        steps = 1
        while r < len(nums) - 1:
            while l <= r:
                farthest = max(farthest, l + nums[l])
                l+=1
            r = farthest
            steps += 1
        return steps