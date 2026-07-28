class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def check(i,crr):
            if crr == amount:
                return 1
            if i == len(coins) or crr > amount:
                return 0
            if (i,crr) in dp:
                return dp[(i,crr)]
            res = check(i, crr + coins[i]) + check(i+1, crr)
            dp[(i,crr)] = res
            return res
        
        return check(0,0)