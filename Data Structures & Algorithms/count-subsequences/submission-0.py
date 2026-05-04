class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def check(i,j):
            if j == len(t):
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            if i == len(s):
                return 0
            res = 0
            if s[i] == t[j]:
                res = check(i+1,j+1)
            res += check(i+1,j)

            dp[(i,j)] = res
            return res

        return check(0,0)