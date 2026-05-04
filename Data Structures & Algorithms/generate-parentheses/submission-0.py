class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(l,r,st):
            nonlocal res
            if l == 0 and r==0:
                st="".join(st)
                res.append(st)
                return
            if l>0:
                helper(l-1,r,st+["("])
                
            if r>0 and r>l:
                helper(l,r-1,st+[")"])
            return
        helper(n,n,[])
        return res
            
