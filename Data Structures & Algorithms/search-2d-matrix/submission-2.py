class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = n * m -1

        while l <= r:
            mid = l + ((r-l)//2)
            row = mid//m
            col = mid%m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return False