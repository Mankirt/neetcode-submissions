class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        d = defaultdict(list)
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                d[i].append((j,dist))
                d[j].append((i,dist))
        length = 0
        visit = set()
        heap = [(0,0)]
        while heap and len(visit) < len(points):
            dist, i = heapq.heappop(heap)
            if i in visit :
                continue
            visit.add(i)
            length += dist
            for neigh, dst in d[i]:
                if neigh not in visit:
                    heapq.heappush(heap, (dst,neigh))
        
        return length