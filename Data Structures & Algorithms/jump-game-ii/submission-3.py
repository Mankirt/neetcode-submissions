class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        nextL = r+1
        nextR = r+1
        jump = 0
        while l<=r and r < len(nums)-1:
            nextR = max(nextR,nums[l]+l)
            if l == r:
                l = nextL
                r = nextR
                jump += 1
                if nextR >= len(nums) - 1:
                    break
                continue
            l+=1
        return jump