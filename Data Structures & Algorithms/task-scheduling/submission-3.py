class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        heap =[]
        for ch in c:
            heapq.heappush(heap,-c[ch])
        
        q = deque([])
        time = 0
        while heap or q:
            time += 1
            while q and q[0][1] <=time:
                heapq.heappush(heap,q.popleft()[0])
            if heap:
                fre = heapq.heappop(heap)
                if fre + 1:
                    q.append([fre+1,time+n+1])
        
        return time