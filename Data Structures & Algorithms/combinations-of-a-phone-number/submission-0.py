class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        l=[]
        d={ "2":'abc','3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def dfs(i):
            if i==len(digits):
                ans.append("".join(l))
                return
            for st in d[digits[i]]:
                l.append(st)
                dfs(i+1)
                l.pop()
            return
        if digits=="":
            return ans
        dfs(0)
        return ans