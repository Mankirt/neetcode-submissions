class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {")": "(", "]":"[", '}': '{'}
        for brct in s:
            if brct in ['(', '[', '{']:
                st.append(brct)
            else:
                if st and st[-1] == d[brct]:
                    st.pop()
                else:
                    return False
        
        return len(st) == 0