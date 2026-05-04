class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        new_deadend = set()
        for dead in deadends:
            t = [int(ch) for ch in dead]
            new_deadend.add(tuple(t))
        target = tuple([int(ch) for ch in target])
        if target in new_deadend or (0,0,0,0) in new_deadend : return -1
        
        dr = [(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)]
        q = deque([(0,0,0,0)])
        t = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == target:
                    return t
                for d1, d2, d3, d4 in dr:
                    new_node = ((node[0]+d1)%10, (node[1]+d2)%10, (node[2]+d3)%10, (node[3]+d4)%10)
                    if new_node not in new_deadend:
                        q.append(new_node)
                        new_deadend.add(new_node)
            t+=1
        return -1