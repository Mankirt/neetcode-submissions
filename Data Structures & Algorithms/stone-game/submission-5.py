class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(i,j):
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = max(piles[i] - dfs(i+1,j), piles[j] - dfs(i,j-1))
            return dp[(i,j)]
        
        return dfs(0,len(piles)-1) > 0 