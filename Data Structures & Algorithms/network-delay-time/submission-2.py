class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj = defaultdict(list)

        for src, des, time in times:
            adj[src].append([des,time])
        visit = set()
        heap = [(0,k)]
        t = 0
        while heap:

                time, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                t = max(t,time)
                for neigh, tt in adj[node]:
                    if neigh not in visit:
                        heapq.heappush(heap, (time+tt,neigh))
        
        return t if len(visit) ==n else -1