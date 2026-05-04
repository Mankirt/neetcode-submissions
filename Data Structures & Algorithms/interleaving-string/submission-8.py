class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [False] * (len(s2) + 1)
        dp[len(s2)] = True   # base case: both strings exhausted
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                
                if i == len(s1) and j == len(s2):
                    continue
                
                take_s1 = False
                take_s2 = False
                
                if i < len(s1) and s1[i] == s3[i + j]:
                    take_s1 = dp[j]   # dp[i+1][j]
                
                if j < len(s2) and s2[j] == s3[i + j]:
                    take_s2 = dp[j+1] # dp[i][j+1]
                
                dp[j] = take_s1 or take_s2
        
        return dp[0]