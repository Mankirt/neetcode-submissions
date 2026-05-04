class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i:set() for i in range(9)}
        col = {i:set() for i in range(9)}
        grid={i:{j:set() for j in range(3)} for i in range(3)}

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue
                elif item not in row[i] and item not in col[j] and item not in grid[i//3][j//3]:
                    row[i].add(item)
                    col[j].add(item)
                    grid[i//3][j//3].add(item)
                
                else:
                    return False
        
        return True