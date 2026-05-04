class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s): return 0
        dp = [[0]*(len(t)+1) for i in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][-1] = 1

        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
                dp[i][j] += dp[i+1][j]
        
        return dp[0][0]




        
        dp = {}
        def find(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j==len(t):
                return 1
            if i==len(s):
                return 0

            res = 0
            if s[i] == t[j]:
                res += find(i+1,j+1)
            res += find(i+1,j) 
            dp[(i,j)] = res
            return res

        return find(0,0)