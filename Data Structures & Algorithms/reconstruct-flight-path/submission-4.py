class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, des in tickets:
            adj[src].append(des)
        
        for key in adj:
            adj[key] = sorted(adj[key])
        
        arr = ["JFK"]
        res = []
        def backtrack(crr):
            if len(arr) == len(tickets) + 1:
                nonlocal res
                res = arr.copy()
                return True
            
            for j in range(len(adj[crr])):
                next_airport = adj[crr][j]
                del adj[crr][j]
                arr.append(next_airport)
                if backtrack(next_airport): return True
                arr.pop()
                adj[crr].insert(j, next_airport)
            return False
        backtrack("JFK")
        return res