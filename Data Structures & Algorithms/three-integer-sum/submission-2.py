class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        ans = []
        while i < len(nums):
            p1 = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if p1 + nums[l] + nums[r] == 0:
                    ans.append([p1,nums[l],nums[r]])
                    while l < len(nums)-1 and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                elif p1 + nums[l] +nums[r] < 0:
                    l +=1
                else:
                    r-=1
            while i< len(nums)-1 and nums[i]==nums[i+1]:
                        i+=1
            i+=1
        
        return ans
                
            