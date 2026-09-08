class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []

        new_start = intervals[0][0]
        new_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start > new_end:
                ans.append([new_start, new_end])
                new_start = start
                new_end = end
                continue
            if new_start < end:
                new_start = min(new_start,start)
                new_end = max(new_end, end)
            else:
                ans.append([start,end])
        ans.append([new_start, new_end])
        return ans