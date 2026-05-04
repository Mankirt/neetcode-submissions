class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        

        def find(i,j,k):
            if k == len(word):
                return True
            if (i,j) in visit or i<0 or j<0 or i >= len(board) or j >=len(board[0]) or board[i][j] != word[k] :
                return False
            
            visit.add((i,j))

            result =  find(i+1,j,k+1) or find(i,j+1,k+1) or find(i-1,j,k+1) or find(i,j-1,k+1)

            visit.remove((i,j))

            return result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visit = set()
                if find(i,j,0): return True
        
        return False

            