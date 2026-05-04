class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i,e in enumerate(equations):
            adj[e[0]].append([e[1],values[i]])
            adj[e[1]].append([e[0],1/values[i]])
        

        def dfs(src,des):
            if src not in adj or des not in adj:
                return -1.0
            visit = set()
            q = [[src,1]]
            visit.add(src)
            while q:
                node , val = q.pop()
                if node == des:
                    return val
                for neigh, mul_val in adj[node]:
                    if neigh not in visit:
                        q.append([neigh,val*mul_val])
                        visit.add(neigh)
            return -1.0

        

        return [dfs(q1,q2) for q1,q2 in queries]