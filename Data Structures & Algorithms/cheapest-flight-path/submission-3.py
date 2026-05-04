class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list)
        for sr, des, price in flights:
            d[sr].append((des,price))
        
        heap = [(0,0,src)] #price, k, src
        visit = set()
        while heap:
            price, stop, airport = heapq.heappop(heap)
            if airport == dst:
                return price
            if stop == k + 1:
                continue
            visit.add(airport)
            for neigh, next_price in d[airport]:
                if neigh not in visit:
                    heapq.heappush(heap, (price + next_price, stop +1, neigh))
        
        return -1