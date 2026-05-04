class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        for i in range(len(capital)):
            capital[i] = [capital[i],profits[i]]
        
        capital.sort(key= lambda x:x[0])
        capital = deque(capital)
        heap = []
        print(capital)
        while (heap or capital) and k >0:
            while capital and w >= capital[0][0]:
                node = capital.popleft()
                heapq.heappush(heap,-node[1])
            if not heap:
                break
            w += (-1*heapq.heappop(heap))
            k-=1
        
        return w