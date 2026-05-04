class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        res = []
        for i,v in enumerate(nums):
            while stack and v >= stack[-1][0]:
                stack.pop()
            stack.append([v,i])
            while stack[0][1]<=i-k:
                stack.pop(0)
            if i >= k-1:
                res.append(stack[0][0])
            #print(i,stack, res)

        return res

        