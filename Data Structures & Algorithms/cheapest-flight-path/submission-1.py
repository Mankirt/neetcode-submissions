class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for srcc, des, price in flights:
            adj[srcc].append([des,price])

        heap = [(0,0,src)] #price, k , src

        while heap:
            price, k_check, srcc = heapq.heappop(heap)
            if srcc == dst and k_check <= k+1:
                return price
            if k_check > k :
                continue
            
            for neigh, p in adj[srcc]:

                heapq.heappush(heap, (price + p,k_check+1, neigh))
        
        return -1