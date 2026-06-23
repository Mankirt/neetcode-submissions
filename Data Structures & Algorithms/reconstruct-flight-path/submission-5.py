class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        d = defaultdict(list)

        for src, des in tickets:
            d[src].append(des)
        
        res = []
        def dfs(node):
            if len(res) == len(tickets):
                return True
            
            for j in range(len(d[node])) :
                temp = d[node][j]
                del d[node][j]
                res.append(temp)
                if dfs(temp): return True
                res.pop()
                d[node].insert(j,temp)
            return False
        
        dfs("JFK")
        return ["JFK"] + res
            
                
            