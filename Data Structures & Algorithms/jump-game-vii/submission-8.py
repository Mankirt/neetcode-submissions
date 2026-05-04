class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        q = deque([0])
        farthest = 0
        n = len(s)
        while q:
            ind = q.popleft()
            start = max(farthest+1,ind+minJump)
            end = min(n-1, ind + maxJump)
            for i in range(start, end + 1):
                if i == n - 1:
                    return True
                if s[i] == '0' :
                    q.append(i)
            farthest = end
        return False
