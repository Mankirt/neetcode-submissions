class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = {(len(s),len(p)):True}

        def check(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if  j ==len(p) :
                return False
            
            if i == len(s) and ((j+1 < len(p) and p[j+1] !='*') or j==len(p)-1):
                return False
            
            if j+1 < len(p) and p[j+1] == "*":
                if i < len(s):
                    if s[i] == p[j] or p[j] == '.':
                        res = check(i+1,j) or check(i,j+2) or check(i+1, j+2)
                    else:
                        res =check(i,j+2)          
                else:
                    res = check(i,j+2)
            elif p[j] == ".":
                res = check(i+1,j+1)
            else:
                if s[i]!=p[j]:
                    res = False
                else:
                    res = check(i+1,j+1)
            
            dp[(i,j)] = res
            return res
        
        return check(0,0)