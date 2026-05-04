class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i,val):
            if i>=len(coins) or val > amount:
                return 0
            if val == amount:
                return 1
            if (i,val) in dp:
                return dp[(i,val)]
            coin = dfs(i,val+coins[i]) + dfs(i+1,val)
            dp[(i,val)] =coin
            return coin

        return dfs(0,0)  