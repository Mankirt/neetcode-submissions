class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = {(len(s),len(p)):True}
        def check(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j == len(p) or (i == len(s) and ((j+1 < len(p) and p[j+1] !='*') or j==len(p)-1)):
                return False
            
            res = False
            if j+1 < len(p) and p[j+1] == '*':
                if i < len(s):
                    if p[j] == '.' or s[i] == p[j]:
                        res = check(i+1,j) or check(i+1, j+2) or check(i, j+2)
                    else:
                        res = check(i,j+2)
                else:
                    res = check(i,j+2)
            elif p[j] == '.' or s[i] == p[j]:
                res = check(i+1,j+1)
            
            
            
            dp[(i,j)] = res
            return res
        
        return check(0,0)
            