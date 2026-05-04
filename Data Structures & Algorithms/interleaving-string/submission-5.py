class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) > len(s3):
            return False
        memo = {}
        
        def backtrack(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == len(s1):
                result = s3[i + j:] == s2[j:]
            elif j == len(s2):
                result = s3[i + j:] == s1[i:]
            else:
                result = (s3[i + j] == s1[i] and backtrack(i + 1, j)) or \
                         (s3[i + j] == s2[j] and backtrack(i, j + 1))
            
            memo[(i, j)] = result
            return result

        return backtrack(0, 0)

