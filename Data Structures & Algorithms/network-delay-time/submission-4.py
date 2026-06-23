class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for u, v, t in times:
            d[u].append((t, v)) #time, v

        heap = [[0,k]] # t, v
        visit = set()
        while heap:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n: return time
            for t, neigh in d[node]:
                if neigh not in visit:
                    heapq.heappush(heap, [time + t, neigh])
        return -1

