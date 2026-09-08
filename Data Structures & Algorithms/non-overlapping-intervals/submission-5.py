class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ans = 0

        start = intervals[0][0]
        end = intervals[0][1]

        for next_start, next_end in intervals[1:]:
            if next_start < end:
                ans += 1
                if next_end < end:
                    start = next_start
                    end = next_end
                continue
            start = next_start
            end = next_end
        
        return ans