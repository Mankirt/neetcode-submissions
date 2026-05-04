class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def backtrack(i, j):
            if i == len(s1):
                return s3[i + j:] == s2[j:]
            if j == len(s2):
                return s3[i + j:] == s1[i:]

            if s3[i + j] == s1[i] and backtrack(i + 1, j):
                return True
            if s3[i + j] == s2[j] and backtrack(i, j + 1):
                return True

            return False

        return backtrack(0, 0)
