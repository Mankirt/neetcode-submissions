"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st = []
        en = []
        for obj in intervals:
            st.append(obj.start)
            en.append(obj.end)
        
        st.sort()
        en.sort()

        ans = 0
        crr = 0
        i = 0
        j = 0
        while i<len(st):
            if st[i] < en[j]:
                crr += 1
                i+=1
            else:
                crr -= 1
                j += 1
            ans = max(ans,crr)
        
        return ans