class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d_s = {")":"(","}":'{',']':"["}
        for op in s:
            if op in d_s:
                if not stack or stack[-1] != d_s[op]:
                    return False
                stack.pop()
            else:
                stack.append(op)
        return True if len(stack)==0  else False