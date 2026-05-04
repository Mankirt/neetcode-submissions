class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(s,i,j,k):
            if k==len(word):
                return True
            if not (0<=i<len(board)) or not (0<=j<len(board[0])) or (i,j) in s or board[i][j]!=word[k]:
                return False
            s.add((i,j))
            result= check(s,i+1,j,k+1) or check(s,i-1,j,k+1) or check(s,i,j+1,k+1) or check(s,i,j-1,k+1)
            s.remove((i,j))
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    s=set()
                    if check(s,i,j,0):
                        return True
        return False