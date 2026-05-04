class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d= {")":"(","}":"{","]":"["}
        for ch in s:
            if ch in d:
                if len(st) == 0:
                    return False
                if st[-1] == d[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        
        return True if len(st) == 0 else False