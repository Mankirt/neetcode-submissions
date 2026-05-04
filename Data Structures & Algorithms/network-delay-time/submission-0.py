class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)

        for src,des,time in times:
            d[src].append([time,des])

        q = [[0,k]]
        visit = set()
        res = 0
        while q:
            t,i = heapq.heappop(q)
            if i not in visit:
                res = max(res,t)
                visit.add(i)

                for t_n, neigh in d[i]:
                    if neigh not in visit:
                        heapq.heappush(q,[t_n+t,neigh])
        
        return res if len(visit)==n else -1