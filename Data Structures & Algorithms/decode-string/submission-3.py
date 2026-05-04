class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        for ch in s:
            if ch == ']':
                temp_string = []
                while st[-1] != '[':
                    temp_string.append(st.pop())
                st.pop()
                val = []
                while st and not ('a'<= st[-1] <='z') and st[-1]!='[':
                    val.append(st.pop())
                val = int("".join(val[::-1]))
                st.extend((temp_string[::-1])*val)
            else:
                st.append(ch)
        
        return "".join(st)