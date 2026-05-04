class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        st =[]
        def check(l,r):
            if l==0 and r==0:
                res.append("".join(st))
                return
            if l>0:
                st.append("(")
                check(l-1,r)
                st.pop()
            if r>0 and r>l:
                st.append(")")
                check(l,r-1)
                st.pop()
        check(n,n)
        return res
            
