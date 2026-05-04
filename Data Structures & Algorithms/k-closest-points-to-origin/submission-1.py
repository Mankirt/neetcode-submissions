class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        heapq.heapify(h)

        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(h,(dist,[x,y]))
        ans = []
        for i in range(k):
            d, p = heapq.heappop(h)
            ans.append(p)
        return ans