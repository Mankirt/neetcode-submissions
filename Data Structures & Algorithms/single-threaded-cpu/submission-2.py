class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,v in enumerate(tasks):
            tasks[i].append(i)
        tasks.sort()
        tasks = deque(tasks)
        heap = []
        time = 0
        ans= []
        while heap or tasks:
            time+=1
            while tasks and tasks[0][0] <= time:
                t, dur, ind = tasks.popleft()
                heapq.heappush(heap,[dur,ind])
            if heap:
                dur, ind = heapq.heappop(heap)
                time += dur - 1
                ans.append(ind)
            else:
                time = tasks[0][0] - 1
        
        return ans
        