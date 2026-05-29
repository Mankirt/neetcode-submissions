class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        for key in count:
            heapq.heappush(heap, -count[key])
        t = 0
        q = deque([]) # [t,fre]

        while heap or q:
            if not heap and t < q[0][0]:
                t = q[0][0]
            while q and t >= q[0][0]:
                time, fre = q.popleft()
                heapq.heappush(heap, fre)
                
            fre_popped = heapq.heappop(heap)
            if fre_popped < -1:
                q.append([t + n + 1, fre_popped + 1])
            
            t += 1
        
        return t