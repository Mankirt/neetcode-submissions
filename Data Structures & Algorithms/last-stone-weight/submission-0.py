class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[]
        heapq.heapify(h)
        for stone in stones:
            heapq.heappush(h,-stone)
        while len(h)>1:
            v1 = heapq.heappop(h)
            v2= heapq.heappop(h)
            heapq.heappush(h,-abs(v1-v2))
        return -h[0]