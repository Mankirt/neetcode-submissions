class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        st = []
        for op in l:
            if op == '.':
                continue
            elif op == '..':
                if len(st)>0:
                    st.pop()
            elif op != '':
                st.append(op)
        
        
        return "/".join([""]+st) if len(st)>0 else "/"
            
