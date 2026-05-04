class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, des, time in times:
            adj[src].append((des,time))
        
        heap = [(0,k)]
        visit = set()
        res_time = -1
        while heap and len(visit)<n:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            res_time = max(res_time, time)
            for neigh, t in adj[node]:
                if neigh not in visit:
                    heapq.heappush(heap, (time + t, neigh))
        
        return res_time if len(visit) == n else -1
