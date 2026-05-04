class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                v, ind = stack.pop()
                ans[ind] = i-ind
            stack.append([t,i])
        return ans 