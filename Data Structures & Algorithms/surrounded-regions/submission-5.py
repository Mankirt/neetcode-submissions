class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        def dfs(i,j):
            if not 0<=i<row or not 0<=j<col or board[i][j] != 'O':
                return
            board[i][j] = 'S'
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
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
            