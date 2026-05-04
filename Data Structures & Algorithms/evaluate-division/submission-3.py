class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list) # a -> b , val

        for i, pair in enumerate(equations):
            src, des = pair
            adj[src].append([des, values[i]])
            adj[des].append([src, 1/values[i]])
        
        def bfs(src, des):
            if src not in adj or des not in adj:
                return -1.0
            
            q = deque([[src, 1.0]]) # src, wt
            visit = set()
            visit.add(src)
            while q:
                node, wt = q.popleft()
                if node == des:
                    return wt
                
                for neigh, weight in adj[node]:
                    if neigh not in visit:
                        q.append([neigh, wt* weight])
                        visit.add(neigh)
            return -1.0

        return [bfs(src, des) for src, des in queries]