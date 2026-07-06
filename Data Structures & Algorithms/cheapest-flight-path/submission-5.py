class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list)

        for st, end, price in flights:
            d[st].append((end, price))   # (des, price)
        
        heap = [[0, 0, src]] #  crr_price, k, airport
        visit = set()
        while heap:
            crr_price, stop, airport = heapq.heappop(heap)
            if stop > k + 1:
                continue
            if airport == dst:
                return crr_price
            
            visit.add(airport)

            for des, price in d[airport]:
                if des not in visit:
                    heapq.heappush(heap, (price + crr_price, stop + 1, des ))
        
        return -1