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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words).root
        visit = set()
        row = len(board)
        col = len(board[0])
        res = set()
        def dfs(i,j, crr_word, node):
            if i<0 or j<0 or i==row or j==col or (i,j) in visit or board[i][j] not in node.children:
                return
            visit.add((i,j))
            node = node.children[board[i][j]]
            crr_word += board[i][j]
            if node.ends:
                res.add(crr_word)
            dfs(i+1,j,crr_word,node)
            dfs(i-1,j,crr_word,node)
            dfs(i,j-1,crr_word,node)
            dfs(i,j+1,crr_word,node)
            visit.remove((i,j))
        
        for i in range(row):
            for j in range(col):
                dfs(i,j,"",trie)
        return list(res)