class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        arr = []

        def create(op,cl):
            if op == 0 and cl == 0:
                ans.append("".join(arr))
                return
            
            if op:
                arr.append("(")
                create(op - 1, cl)
                arr.pop()
            
            if cl > op:
                arr.append(")")
                create(op, cl - 1)
                arr.pop()
        create(n,n)
        return ans