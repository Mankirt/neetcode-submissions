class Trie:
    def __init__(self):
        self.children = {}
        self.ends = False
        self.word = ''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            crr = root
            for ch in word:
                if ch not in crr.children:
                    crr.children[ch] = Trie()
                crr = crr.children[ch]
            crr.ends = True
            crr.word = word

        row = len(board)
        col = len(board[0])
        ans = []
        visit = set()
        dr = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j,node):
            if not(0<=i<row) or not(0<=j<col):
                return
            if node.ends:
                ans.append(node.word)
                node.ends = False
            for dx, dy in dr:
                x = i + dx
                y = j + dy
                if (0<=x<row) and (0<=y<col) and (x,y) not in visit and board[x][y] in node.children:
                    visit.add((x,y))
                    dfs(x,y,node.children[board[x][y]])
                    visit.remove((x,y))
            
            


        for i in range(row):
            for j in range(col):
                ch = board[i][j]
                if ch in root.children:
                    visit.add((i,j))
                    dfs(i,j,root.children[ch])
                    visit.remove((i,j))
        
        return ans