"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()
        ans = 0
        crr = 0
        i = j = 0
        while i < len(start):
            if end[j] <= start[i]:
                crr -= 1
                j += 1
            else:
                crr += 1
                i += 1
                ans = max(ans,crr)
        return ans
