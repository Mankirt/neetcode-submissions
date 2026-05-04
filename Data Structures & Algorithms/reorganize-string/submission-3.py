class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        heap = []
        for key in c:
            heapq.heappush(heap,[-c[key], key])
        crr = []
        ans = []
        while heap or crr:
            if not heap:
                return ""
            fre, ch = heapq.heappop(heap)
            ans.append(ch)
            if len(crr)>0:
                heapq.heappush(heap,crr)
            crr = [fre+1, ch] if fre + 1 < 0 else []

        return "".join(ans)
        