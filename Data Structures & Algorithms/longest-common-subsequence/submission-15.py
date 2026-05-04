class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0]* (m+1) for i in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max( dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]






        dp = {}
        def backtrack(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res = 0
            if text1[i] == text2[j]:
                res = 1 + backtrack(i+1,j+1)
            res = max(res, 
            backtrack(i+1, j),
            backtrack(i, j+1))
            dp[(i,j)] = res
            return res
        return backtrack(0,0)
        
            