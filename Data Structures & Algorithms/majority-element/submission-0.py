class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        val = 1
        for i in range(1,len(nums)):
            if nums[i] == ans:
                val+=1
            else:
                val -=1
                if val == 0:
                    ans = nums[i]
                    val = 1
        return ans