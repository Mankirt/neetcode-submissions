class Solution:
    def maxDifference(self, s: str) -> int:
        counter  = Counter(s)

        even_min = float('inf')
        odd_max = 0

        for key in counter:
            fre = counter[key]
            if fre % 2:
                odd_max = max(odd_max, fre)
            else:
                even_min = min(even_min, fre)
        
        return odd_max - even_min
