class Solution:
    def checkValidString(self, s: str) -> bool:
        max_left = min_left = 0

        for ch in s:
            if ch == '(':
                max_left += 1
                min_left += 1
            elif ch == ')':
                max_left -= 1
                if max_left < 0: return False
                min_left = max(0,min_left - 1)
            else:
                max_left += 1
                min_left = max(0,min_left - 1)
        return min_left == 0
