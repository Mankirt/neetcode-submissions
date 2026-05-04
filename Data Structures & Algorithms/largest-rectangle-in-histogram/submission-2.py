class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0

        stack = []

        for i,v in enumerate(heights):
            start = i
            while stack and stack[-1][0] >= v:
                val, start =stack.pop()
                ans = max(ans, (i-start)*val)
            stack.append([v,start])
        print(stack)
        for i in range(len(stack)):
            ans = max(ans,(len(heights)-stack[i][1])*stack[i][0])
        
        return ans
