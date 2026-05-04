class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        crr_max = 1
        crr_min = 1
        res = max(nums)
        for num in nums:
            if num == 0:
                crr_max = 1
                crr_min = 1
            else:
                temp = crr_max
                crr_max = max(crr_max * num, crr_min * num, num)

                crr_min = min(temp * num, crr_min *num, num)

                res = max(res,crr_max)
        return res