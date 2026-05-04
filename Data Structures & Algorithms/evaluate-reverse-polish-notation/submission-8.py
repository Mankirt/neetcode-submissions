class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == '+':
                st.append(st.pop()+st.pop())
            elif t=='-':
                temp = st.pop()
                st.append(st.pop()-temp)
            elif t == '*':
                st.append(st.pop()*st.pop())
            elif t == '/':
                temp = st.pop()
                st.append(int(st.pop()/temp))
            else:
                st.append(int(t))
        
        return st[0]