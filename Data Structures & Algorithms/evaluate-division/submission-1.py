

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)

        for i,v in enumerate(equations):
            src, des = v
            d[src].append([des,values[i]])
            d[des].append([src,1/values[i]])
        

        def bfs(src,des):
            if src not in d or des not in d:
                return -1.0
            q = [[src,1]]
            visit = set()
            visit.add(src)
            while q:
                node, val = q.pop(0)
                if node == des:
                    return val
                for neigh, inter_val in d[node]:
                    if neigh not in visit:
                        q.append([neigh,val*inter_val])
                        visit.add(neigh)
            return -1.0
                

        




        return [bfs(src,des) for src,des in queries]

