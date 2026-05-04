class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        arr = []
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(arr))
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    arr.append(s[i:j+1])
                    backtrack(j+1)
                    arr.pop()
            return
        
        backtrack(0)
        return res
