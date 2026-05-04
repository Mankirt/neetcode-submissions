class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def dfs(crr, visit, path, order, adj):
            if crr in path:
                return False
            if crr in visit:
                return True
            visit.add(crr)
            path.add(crr)
            for neigh in adj[crr]:
                if not dfs(neigh, visit, path, order, adj): return False
            
            path.remove(crr)
            
            order.append(crr)
            return True



        def topo_sort(arr):
            adj = defaultdict(list)
            order = []
            visit = set()
            path = set()
            for src, des in arr:
                adj[src].append(des)
            
            for i in range(1,k+1):
                if i not in visit:
                    if not dfs(i,visit, path, order, adj): return []

            return order[::-1]
        

        
        row_value = topo_sort(rowConditions)
        col_value = topo_sort(colConditions)
        if not row_value or not col_value:
            return []

        row_map  = { v:i for i, v in enumerate(row_value)}
        col_map  = { v:i for i, v in enumerate(col_value)}

        res = [[0]*k for i in range(k)]

        for i in range(1,k+1):
            r = row_map[i]
            c = col_map[i]
            res[r][c] = i
        
        return res