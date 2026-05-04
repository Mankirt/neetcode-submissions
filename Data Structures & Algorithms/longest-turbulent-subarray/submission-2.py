class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        crr = 1
        sign = 0
        prev = arr[0]
        for item in arr[1:]:
            if sign == 1:
                if item > prev:
                    crr += 1
                    sign = -1
                elif item < prev:
                    crr = 2
                else:
                    sign = 0
                    crr = 1
            elif sign == -1:
                if item < prev:
                    crr += 1
                    sign  = 1
                elif item > prev:
                    crr = 2
                else:
                    sign = 0
                    crr = 1
            else:
                if item > prev:
                    sign = -1
                    crr += 1
                elif item < prev:
                    sign = 1
                    crr += 1
                else:
                    crr = 1
            prev = item
            ans = max(ans,crr)
        
        return ans

