class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mn = nums[0]
        res = mx
        for num in nums[1:]:
            if num == 0:
                mx = mn = 1
            temp = mx
            mx = max(mx * num, mn * num, num)
            mn = min(temp* num, mn * num, num)
            res = max(res, mx)
        return res