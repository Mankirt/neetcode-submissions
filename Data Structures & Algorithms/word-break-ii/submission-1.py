class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        arr = []

        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                copy = " ".join(arr)
                res.append(copy)
                return
            
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict:
                    arr.append(s[i:j+1])
                    backtrack(j+1)
                    arr.pop()
        backtrack(0)
        return res