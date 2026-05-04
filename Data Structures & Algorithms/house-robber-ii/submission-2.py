class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        def check(arr):
            a = 0
            b = arr[-1]
            c = arr[-2] 
            for i in range(len(arr)-3,-1,-1):
                temp = arr[i] + max(a,b)
                a = b
                b = c
                c = temp
            return max(b,c)

        return max(check(nums[:-1]),check(nums[1:]))