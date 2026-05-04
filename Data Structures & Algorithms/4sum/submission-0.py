class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        i = 0
        ans = []
        while i < len(nums):
            j = i+1
            while j<len(nums):
                k = j + 1
                l = len(nums) -1

                while k < l:
                    if nums[i] + nums[j] + nums[k] +nums[l] == target:
                        ans.append([nums[i], nums[j],nums[k],nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k+=1
                        k+=1
                    elif nums[i] + nums[j] + nums[k] +nums[l] < target:
                        k+=1
                    else:
                        l-=1
                while j<len(nums)-1 and nums[j]==nums[j+1]:
                    j+=1
                j+=1
            while i< len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return ans
            