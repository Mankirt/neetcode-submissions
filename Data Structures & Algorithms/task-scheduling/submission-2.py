class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l=[0]*26
        for task in tasks:
            l[ord(task)-ord('A')]+=1
        
        h=[]
        heapq.heapify(h)
        for task in l:
            if task:
                heapq.heappush(h,-task)
        m=-heapq.heappop(h)
        extra_space = (m-1)* n
        while h:
            aa=-heapq.heappop(h)
            if aa == m:
                extra_space-=m-1
            else:
                extra_space-= aa
        return len(tasks)+extra_space if extra_space>0 else len(tasks)
