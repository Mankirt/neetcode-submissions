class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0]*len(temperatures)
        stack=[]
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0]<v:
                temp_res=stack.pop()
                res[temp_res[1]]=i-temp_res[1]
            stack.append((v,i))
        return res