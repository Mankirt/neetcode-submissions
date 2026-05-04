class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1,len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                d[i].append([j,dist])
                d[j].append([i,dist])
        
        q = [[0,0]]
        visit = set()
        res = 0
        while q:
            dis, node = heapq.heappop(q)
            if node in visit:
                continue
            visit.add(node)
            res += dis
            for neigh, x in d[node]:
               
                    heapq.heappush(q,[x,neigh])
        return res