class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visit = set(deadends)
        if '0000' in visit:
            return -1
        q = [["0000",0]]
        visit.add("0000")

        def children(pattern):
            child = []
            for i in range(4):
                child.append(pattern[:i]+ str((int(pattern[i])+1)%10) +pattern[i+1:])
                child.append(pattern[:i]+ str((int(pattern[i])-1+10)%10) +pattern[i+1:])
            return child



        while q:
            for i in range(len(q)):
                pattern, moves = q.pop(0)
                if pattern == target:
                    return moves
                for child in children(pattern):
                    if child not in visit:
                        q.append([child,moves+1])
                        visit.add(child)
        return -1
                