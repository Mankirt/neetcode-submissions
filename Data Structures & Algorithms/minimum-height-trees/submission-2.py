class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        d = defaultdict(set)
        for src, des in edges:
            d[src].add(des)
            d[des].add(src)
        
        while len(d) > 2:
            remove = []
            for key in d:
                if len(d[key]) == 1:
                    remove.append(key)
            for key in remove:
                for node in list(d[key]):
                    d[node].remove(key)                  
                del d[key]
        
        return list(d.keys())