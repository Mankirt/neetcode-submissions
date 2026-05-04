class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = len(s)-1
        while i>=0:
            l = i
            if '0'<= s[l] <= '9' :
                while i>0 and '0'<= s[i-1] <= '9':
                    i-=1
                stack.pop()
                temp = []
                while stack[-1]!="]":
                    temp.append(stack.pop())
                stack.pop()
                stack.append("".join(temp)*int(s[i:l+1]))
            else:
                stack.append(s[i])
            i-=1
        return "".join(stack[::-1])

                