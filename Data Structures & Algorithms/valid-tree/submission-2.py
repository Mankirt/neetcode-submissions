class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle = set()
        d = defaultdict(list)
        for x,y in edges:
            d[x].append(y)
            d[y].append(x)

        def check(i, last):
            if i in cycle:
                return False
            cycle.add(i)
            for neigh in d[i]:
                if neigh != last:
                    if not check(neigh, i):   
                        return False
            
            return True
        
        return check(0,-1) and len(cycle)==n