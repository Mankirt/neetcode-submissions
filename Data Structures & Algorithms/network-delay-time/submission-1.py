class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for src,des,t in times:
            d[src].append([des,t])
        
        q = [[0,k]]
        visit = set()
        visit.add(k)
        while q:
            t, node = heapq.heappop(q)
            visit.add(node)
            if len(visit) == n:
                return t
            for neigh in d[node]:
                if neigh[0] not in visit:
                    heapq.heappush(q,[t+neigh[1],neigh[0]])
                    
        return -1