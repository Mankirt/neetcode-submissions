class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapq.heapify(h)
        for st in stones:
            heapq.heappush(h,-st)
        while len(h)>1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)
            if a!=b:
                heapq.heappush(h,-(a-b))
        return -h[0] if len(h)==1 else 0

