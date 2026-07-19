class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        # for i in range(len(text1) + 1):
        #     dp[i][-1] = 1
        # for j in range(len(text2) + 1):
        #     dp[-1][j] = 
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                res = 0
                if text1[i] == text2[j]:
                    res = 1 + dp[i+1][j+1]
                res = max(res, dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                dp[i][j] = res
        return dp[0][0]

        dp = {}

        def check(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            re = 0
            if text1[i] == text2[j]:
                re = 1 + check(i+1,j+1)
            
            re = max(re, check(i+1,j), check(i,j+1), check(i+1, j+1))
            dp[(i,j)] = re
            return re
        
        return check(0,0)