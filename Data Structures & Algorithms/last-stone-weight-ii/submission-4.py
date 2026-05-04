class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)//2
        res = 0
        dp = {}
        def backtrack(i,crr):
            if crr > target:
                return 0
            if (i,crr) in dp:
                return dp[(i,crr)]
            if crr == target or i == len(stones):
                res = crr
            else:
                res = max(
            backtrack(i+1, crr + stones[i]),
            backtrack(i+1, crr))
            dp[(i,crr)] = res
            return res
        
        res = backtrack(0,0)
        print(sum(stones))
        print(res)
        return (sum(stones)-res) - res

            