class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        row_set = set()
        col_set = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        
        for i in row_set:
            for j in range(col):
                matrix[i][j] = 0
        
        for j in col_set:
            for i in range(row):
                matrix[i][j] = 0

        