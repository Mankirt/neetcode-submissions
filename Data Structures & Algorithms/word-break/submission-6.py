class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {}
        wordDict = set(wordDict)
        def backtrack(i):
            if i in d:
                return d[i]
            if i == len(s):
                d[i] = True
                return True
            
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict:
                    if backtrack(j+1): 
                        d[i] = True
                        return True
            
            d[i] = False
            return False
        
        return backtrack(0)