class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.r = len(board)
        self.c = len(board[0])
        visit = set()
        visited = set()

        def check(i,j):
            if not (0<=i<self.r) or not (0<=j<self.c) or (i,j) in visited:
                return
            visited.add((i,j))
            if board[i][j] == 'X':
                return
            
            visit.add((i,j))
            check(i+1,j)
            check(i-1,j)
            check(i,j+1)
            check(i,j-1)
            return

        for i in range(self.r):
            check(i,0)
        
        for i in range(self.r):
            check(i,self.c-1)
        
        for i in range(self.c):
            check(0,i)
        for i in range(self.c):
            check(self.r-1,i)

        for i in range(self.r):
            for j in range(self.c):
                if board[i][j] == 'O' and (i,j) not in visit:
                    board[i][j] = 'X'