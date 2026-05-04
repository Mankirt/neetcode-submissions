class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for s,e in intervals[1:]:
            if s>=prevEnd:
                prevEnd=e
            else:
                res+=1
                prevEnd = min(prevEnd,e)
        return res