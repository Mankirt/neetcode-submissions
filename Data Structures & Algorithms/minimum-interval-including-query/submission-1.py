class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [float('inf') for i in range(10001)]

        for interval in intervals:
            start, end = interval
            l = end-start+1
            for j in range(start,end+1):
                ans[j] = min(ans[j],l)
        
        return [ans[i] if ans[i]!=float('inf') else -1 for i in queries]