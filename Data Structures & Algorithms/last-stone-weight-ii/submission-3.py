class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = (sum(stones)+1)//2
        self.ans = float('inf')
        dp = {}
        def find(i,crr):
            if crr >= target or i ==len(stones):
                return abs((sum(stones)-crr) - crr)
            if (i,crr) in dp:
                return dp[(i,crr)]
            
            dp[(i,crr)] = min(find(i+1,crr) , find(i+1,crr+stones[i]))
            return dp[(i,crr)]
        
        return find(0,0)