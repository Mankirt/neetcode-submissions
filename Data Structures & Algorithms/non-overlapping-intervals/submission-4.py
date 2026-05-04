class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last = intervals[0][1]
        res= 0 

        for st, end in intervals[1:]:
            if st>=last:
                last = end
            else:
                res += 1
                last = min(last,end)
        return res