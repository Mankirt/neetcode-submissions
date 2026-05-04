class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def check(l,r,st):
            if l==0 and r==0:
                res.append("".join(st))
                return
            if l>0:
                check(l-1,r,st+["("])
            if r>0 and r>l:
                check(l,r-1,st+[')'])
        
        check(n,n,[])
        return res
            
