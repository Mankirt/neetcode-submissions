class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        arr = []
        def backtrack(op,close):
            if op == 0 and close == 0:
                ans.append("".join(arr))
                return
            if close < op or op < 0:
                return
            
            arr.append("(")
            backtrack(op-1,close)
            arr.pop()
            arr.append(")")
            backtrack(op,close-1)
            arr.pop()
        
        backtrack(n,n)
        return ans