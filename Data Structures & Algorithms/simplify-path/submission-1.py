class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        stack = []
        for i in range(1,len(l)):
            if l[i] == '..':
                if stack:
                    stack.pop()
            elif l[i] != '.' and l[i]!='':
                stack.append(l[i])
        return "/"+"/".join(stack)