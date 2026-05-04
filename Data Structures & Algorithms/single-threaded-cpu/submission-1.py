class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap1 = []
        for i,v in enumerate(tasks):
            heapq.heappush(heap1,(v[0],v[1],i))
        heap2 = []
        first = heapq.heappop(heap1)
        t = first[0] + first[1]
        ans = [first[2]]
        while heap1:
            while heap1 and heap1[0][0] <= t:
                t1,t2,i = heapq.heappop(heap1)
                heapq.heappush(heap2,(t2,i))
            if heap2:
                t2,i = heapq.heappop(heap2)
                t+=t2
            else:
                t1,t2,i = heapq.heappop(heap1)
                t = t1+t2
            ans.append(i)
        while heap2:
            t2,i = heapq.heappop(heap2)
            ans.append(i)
        
        return ans