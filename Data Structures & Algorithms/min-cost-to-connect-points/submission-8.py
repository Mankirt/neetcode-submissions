class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        d = defaultdict(list)
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                d[i].append((j,dist))
                d[j].append((i,dist))
        visit = set()
        ans = 0
        heap = [(0,0)]
        while heap:
            dist, i = heapq.heappop(heap)
            if i in visit:
                continue
            visit.add(i)
            ans += dist
            if len(visit) == len(points):
                return ans
            for neigh, ecl_dist in d[i]:
                if neigh not in visit:
                    heapq.heappush(heap, (ecl_dist, neigh))
            