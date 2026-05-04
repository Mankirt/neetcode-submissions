"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap_s = []
        heap_e = []

        for interval in intervals:
            heapq.heappush(heap_s,interval.start)
            heapq.heappush(heap_e,interval.end)
        ans = 0
        crr = 0
        while heap_s:
            if heap_s[0] < heap_e[0]:
                heapq.heappop(heap_s)
                crr += 1
            else:
                heapq.heappop(heap_e)
                crr -= 1
            
            ans = max(ans,crr)
        
        return ans
            