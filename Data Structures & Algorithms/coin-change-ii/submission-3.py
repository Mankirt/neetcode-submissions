class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {amount: 1}
        def find(i, crr):
            if crr == amount:
                return 1
            if (i, crr) in dp:
                return dp[(i,crr)]
            if crr > amount or i == len(coins):
                return 0
            
            dp[(i,crr)] = find(i,crr+coins[i]) + find(i+1, crr)
            return dp[(i,crr)]
            
        return find(0,0)