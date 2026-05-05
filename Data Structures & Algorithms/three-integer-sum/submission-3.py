class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i],nums[l], nums[r]])
                    while l+1 < r and nums[l] == nums[l+1] :
                        l += 1
                    l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            while i < len(nums) - 2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ans
                