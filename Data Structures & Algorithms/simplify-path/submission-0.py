class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        stack = []
        for i in range(1,len(l)):
            if l[i] == '.' or l[i]=='':
                continue
            elif l[i] == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(l[i])
        res = "/".join(stack) if stack else ""
        return "/"+res