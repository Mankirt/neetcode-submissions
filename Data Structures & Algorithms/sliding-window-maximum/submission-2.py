class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        ans=[]
        l=0
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            if i-k+1>=0:
                if stack[0]==i-k:
                    stack.pop(0)
                ans.append(nums[stack[0]])
        return ans
        