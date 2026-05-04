class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for cp, st, end in trips:
            heapq.heappush(heap,(st, cp))
            heapq.heappush(heap,(end, -cp))
        res = 0
        while heap :
            res+= heapq.heappop(heap)[1]
            if res>capacity:
                return False
        return True