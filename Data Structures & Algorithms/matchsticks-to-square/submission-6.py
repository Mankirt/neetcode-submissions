class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 : return False
        l = s/4
        if max(matchsticks) > l: return False

        sides = [l] * 4
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] >= matchsticks[i]:
                    sides[j] -= matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] += matchsticks[i]
            return False
        
        return backtrack(0)