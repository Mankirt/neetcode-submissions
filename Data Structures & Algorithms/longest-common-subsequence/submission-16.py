class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

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