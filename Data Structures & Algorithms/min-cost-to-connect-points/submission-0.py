class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x,y = points[i]
            for j in range(len(points)):
                x1, y1 = points[j]
                dist = abs(x-x1) + abs(y-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        

        res = 0
        visit = set()
        minH = [[0,0]]

        while len(visit)<len(points):
            cost, i = heapq.heappop(minH)
            if i not in visit:
                res += cost
                visit.add(i)
                for cost_n, neigh in adj[i]:
                    if neigh not in visit:
                        heapq.heappush(minH, [cost_n, neigh])
        return res