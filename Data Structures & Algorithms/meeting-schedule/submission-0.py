"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        intervals.sort(key  = lambda x:x.start)
        
        for i in range(1,len(intervals)):
            x1 = intervals[i-1]
            x2 = intervals[i]
            if x2.start < x1.end:
                return False
        return True
