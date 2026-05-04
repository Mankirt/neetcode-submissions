class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {(len(word1),len(word2)):0}
        def check(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == len(word1) or j == len(word2):
                return max(len(word1)-i,len(word2)-j)
      
            if word1[i] == word2[j]:
                res = check(i+1,j+1)
            else:
                res = 1 + min(check(i+1,j), check(i,j+1), check(i+1,j+1))
            
            dp[(i,j)] = res
            return res
        
        return check(0,0)