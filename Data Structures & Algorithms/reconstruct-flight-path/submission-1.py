from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph with priority queues
        graph = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)
        
        result = []

        def dfs(node):
            # Visit all destinations in lexical order
            while graph[node]:
                next_node = heapq.heappop(graph[node])
                dfs(next_node)
            result.append(node)

        # Start DFS from "JFK"
        dfs("JFK")
        return result[::-1]  # Reverse to get the correct order
