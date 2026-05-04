class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={")":"(", "}":"{", "]":"["}
        for sym in s:
            if sym in [")",'}',"]"]:
                if stack and stack[-1] == d[sym]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sym)
        if stack:
            return False
        return True