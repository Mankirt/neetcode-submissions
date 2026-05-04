class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0 , len(matrix)*len(matrix[0])-1
        col_n = len(matrix[0])
        while l<=r:
            mid = l + (r-l)//2
            row = mid//col_n
            col = mid%col_n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid+1
            else:
                r = mid - 1
        return False