"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st = sorted([s.start for s in intervals])
        en = sorted([s.end for s in intervals])
        i,j = 0,0
        count = 0
        res = 0
        while i < len(st):
            if st[i] < en[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            res = max(res, count)
        return res