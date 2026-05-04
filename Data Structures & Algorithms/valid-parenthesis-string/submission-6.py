class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_max = 0 # * -> (
        left_min = 0 # * -> ); left_min < 0; =0

        for ch in s:
            if ch == "(":
                left_max += 1
                left_min += 1
            elif ch == ")":
                left_max -= 1
                left_min  = max(0, left_min-1)
                if left_max < 0:
                    return False
            else:
                left_max += 1
                left_min = max(0, left_min-1)

        return left_min == 0 