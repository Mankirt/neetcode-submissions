class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones)>1:
            large = -heapq.heappop(stones)
            small = -heapq.heappop(stones)
            if large-small:
                heapq.heappush(stones,small-large)
        
        return -stones[0] if len(stones) == 1 else 0
