class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        crr = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            if interval[0] < crr:
                res += 1
                crr = min(crr,interval[1])
            else:
                crr = interval[1]
        return res