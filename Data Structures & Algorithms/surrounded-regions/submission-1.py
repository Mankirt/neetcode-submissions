class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        visit = set()

        def dfs(i,j):
            if i<0 or j<0 or i==row or j ==col or (i,j) in visit or board[i][j]!='O':
                return
            board[i][j]="T"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        

        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)

        for j in range(col):
            dfs(0,j)
            dfs(row-1,j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j]=='T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                    