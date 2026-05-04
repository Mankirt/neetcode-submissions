class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        dia1 = set()
        dia2 = set()


        def backtrack(r):
            if r == n :
                return 1
            
            result = 0
            for c in range(n):
                if c in col or r+c in dia1 or r-c in dia2:
                    continue
                
                col.add(c)
                dia1.add(r+c)
                dia2.add(r-c)

                result += backtrack(r+1)

                col.remove(c)
                dia1.remove(r+c)
                dia2.remove(r-c)
            
            return result
        
        return backtrack(0)

        
