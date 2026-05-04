class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False
class Trie:
    def __init__(self,words):
        self.root = TrieNode()
        for word in words:
            crr = self.root
            for w in word:
                if w not in crr.children:
                    crr.children[w] = TrieNode()
                crr = crr.children[w]
            crr.ends = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root
        dp = {len(s):0}
        def backtrack(i):

            if i in dp:
                return dp[i]
            
            res = 1 + backtrack(i+1)
            crr = trie
            for j in range(i,len(s)):
                if s[j] not in crr.children:
                    break
                crr = crr.children[s[j]]
                if crr.ends:
                    res = min(res, backtrack(j+1))
            dp[i] = res
            return res

        return backtrack(0)