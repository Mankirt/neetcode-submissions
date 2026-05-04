import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list)

        for s, des, price in flights:  # Loop to populate adjacency list
            d[s].append([price, des])

        # Priority queue to store [current cost, current stops, current city]
        q = [[0, 0, src]]

        # A dictionary to track the minimum stops for each city
        while q:
            cost, limit, i = heapq.heappop(q)
            
            # If we reached the destination, return the cost
            if i == dst:
                return cost

            # Only continue if we haven't exceeded the stop limit
            if limit <= k:
                for price, neigh in d[i]:
                    heapq.heappush(q, [cost + price, limit + 1, neigh])

        return -1  # If no route is found
