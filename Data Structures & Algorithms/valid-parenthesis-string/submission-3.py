class Solution:
    def checkValidString(self, s: str) -> bool:
        
            leftMax, leftMin = 0 , 0
            for ch in s:
                if ch == ')':
                    leftMax -= 1
                    leftMin -= 1
                elif ch == '(':
                    leftMax += 1
                    leftMin += 1
                else:
                    leftMax += 1
                    leftMin -=1
                if leftMax < 0:
                    return False
                leftMin = max(0,leftMin)
            
            return leftMin == 0
