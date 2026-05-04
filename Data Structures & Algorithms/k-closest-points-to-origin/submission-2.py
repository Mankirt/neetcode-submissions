class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for i,v in enumerate(points):
            d = v[0]**2 + v[1]**2
            dis.append((d,i))
        
        dis.sort()
        res= []
        for i in range(k):
            res.append(points[dis[i][1]])
        return res