class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q= [0]
        far = 0
        while q:
            i = q.pop(0)
            if i == len(s)-1:
                        return True
            start = max(i+minJump, far + 1)
            for j in range(start, min(i+maxJump+1,len(s))):
                if s[j] == '0':
                    q.append(j)
                    
            far = i + maxJump
        return False