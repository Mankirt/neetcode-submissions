class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        visit = set()
        q = deque([0])
        visit.add(0)
        while q:
            ind = q.popleft()
            
            for i in range(ind+minJump,ind+maxJump+1):
                if i >= len(s):
                    break
                if i == len(s) - 1:
                    return True
                if s[i] == '0' and i not in visit:
                    q.append(i)
                    visit.add(i)
        return False
