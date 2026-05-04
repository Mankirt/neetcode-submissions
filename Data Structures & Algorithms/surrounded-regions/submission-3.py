class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque([])
        for i in range(len(board)):
            if board[i][0] == 'O':
                q.append([i,0])
            if board[i][-1] == 'O':
                q.append([i,len(board[0])-1])

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                q.append([0,j])
            if board[-1][j] == 'O':
                q.append([len(board)-1, j])
        
        while q:
            i, j = q.popleft()
            board[i][j] = 'T'
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x = i + dx
                y = j + dy
                if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'O':
                    q.append([x,y])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'