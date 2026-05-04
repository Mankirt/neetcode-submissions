class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        res = []
        for count, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count!= 0:
                heapq.heappush(heap, (count,ch))
        
        while heap:
            count, ch = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not heap:
                    break
                count2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                count2 += 1
                if count2 !=0:
                    heapq.heappush(heap, (count2, ch2))

            else:
                res.append(ch)
                count += 1
            if count!=0:
                heapq.heappush(heap, (count,ch))
        
        return "".join(res)